// Netlify Function: subscribe
// POST /.netlify/functions/subscribe
//
// Flow:
//   1. Validate request (email, first name, consent, honeypot, interests array)
//   2. Apply per-IP rate limit (best-effort, in-memory)
//   3. Generate 4 Scaleway pre-signed URLs (15-min TTL each)
//   4. Push subscriber to MailerLite: main group + per-PDF intent tags (only checked ones)
//   5. Return { success: true, urls: { ... }, expiresIn: 900 }
//
// Intent vs delivery: every subscriber receives all 4 download links in the success state.
// The per-PDF MailerLite tags reflect declared INTEREST (checkboxes), not what they downloaded.
// Actual per-PDF click behaviour is tracked client-side via PostHog `pdf_download` events.

import { S3Client, GetObjectCommand } from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

const URL_TTL_SECONDS = 900;
const RATE_LIMIT_WINDOW_MS = 15 * 60 * 1000;
const RATE_LIMIT_MAX_REQUESTS = 5;

const rateLimitStore = new Map();

function rateLimitCheck(ip) {
  const now = Date.now();
  const bucket = rateLimitStore.get(ip) || [];
  const recent = bucket.filter((ts) => now - ts < RATE_LIMIT_WINDOW_MS);
  if (recent.length >= RATE_LIMIT_MAX_REQUESTS) return false;
  recent.push(now);
  rateLimitStore.set(ip, recent);
  if (rateLimitStore.size > 1000) {
    const cutoff = now - RATE_LIMIT_WINDOW_MS;
    for (const [k, v] of rateLimitStore) {
      const remaining = v.filter((ts) => ts > cutoff);
      if (remaining.length === 0) rateLimitStore.delete(k);
      else rateLimitStore.set(k, remaining);
    }
  }
  return true;
}

function emailValid(s) {
  return typeof s === "string" && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(s) && s.length <= 254;
}

function jsonResponse(status, body) {
  return {
    statusCode: status,
    headers: {
      "Content-Type": "application/json",
      "Cache-Control": "no-store",
    },
    body: JSON.stringify(body),
  };
}

function getS3Client() {
  return new S3Client({
    region: process.env.SCW_REGION,
    endpoint: process.env.SCW_ENDPOINT,
    credentials: {
      accessKeyId: process.env.SCW_ACCESS_KEY,
      secretAccessKey: process.env.SCW_SECRET_KEY,
    },
  });
}

const PDF_ENV_KEYS = {
  "visual-read": "SCW_KEY_VISUAL_READ",
  "long-read": "SCW_KEY_LONG_READ",
  executive: "SCW_KEY_EXECUTIVE",
  specialist: "SCW_KEY_SPECIALIST",
};

// User-facing filename when the browser saves the PDF.
// Bucket object keys can stay programmer-friendly; this overrides at download time.
const PDF_DOWNLOAD_FILENAMES = {
  "visual-read": "European AI Labour Market - Visual Read.pdf",
  "long-read": "European AI Labour Market - Long Read.pdf",
  executive: "European AI Labour Market - Executive.pdf",
  specialist: "European AI Labour Market - Specialist.pdf",
};

const INTEREST_SLUGS = ["visual-read", "long-read", "executive", "specialist"];

const INTEREST_TAG_ENV = {
  "visual-read": "MAILERLITE_TAG_VISUAL_READ",
  "long-read": "MAILERLITE_TAG_LONG_READ",
  executive: "MAILERLITE_TAG_EXECUTIVE",
  specialist: "MAILERLITE_TAG_SPECIALIST",
};

async function presignAll() {
  const s3 = getS3Client();
  const bucket = process.env.SCW_BUCKET;
  const entries = await Promise.all(
    Object.entries(PDF_ENV_KEYS).map(async ([slug, envKey]) => {
      const objectKey = process.env[envKey];
      if (!objectKey) throw new Error(`Missing env var: ${envKey}`);
      const filename = PDF_DOWNLOAD_FILENAMES[slug];
      const cmd = new GetObjectCommand({
        Bucket: bucket,
        Key: objectKey,
        ResponseContentDisposition: `attachment; filename="${filename}"`,
        ResponseContentType: "application/pdf",
      });
      const url = await getSignedUrl(s3, cmd, { expiresIn: URL_TTL_SECONDS });
      return [camelCase(slug), url];
    }),
  );
  return Object.fromEntries(entries);
}

function camelCase(slug) {
  return slug.replace(/-([a-z])/g, (_, c) => c.toUpperCase());
}

async function pushToMailerLite({ email, firstName, lastName, company, jobTitle, interests, ip }) {
  const apiKey = process.env.MAILERLITE_API_KEY;
  if (!apiKey) throw new Error("Missing MAILERLITE_API_KEY");

  const intentTagIds = interests
    .map((slug) => process.env[INTEREST_TAG_ENV[slug]])
    .filter(Boolean);

  const groups = [process.env.MAILERLITE_GROUP_ID, ...intentTagIds].filter(Boolean);

  const fields = {};
  if (firstName) fields.name = firstName;
  if (lastName) fields.last_name = lastName;
  if (company) fields.company = company;
  if (jobTitle) fields.job_title = jobTitle;

  const body = {
    email,
    fields,
    groups,
    ip_address: ip || undefined,
  };

  const resp = await fetch("https://connect.mailerlite.com/api/subscribers", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      Authorization: `Bearer ${apiKey}`,
    },
    body: JSON.stringify(body),
  });

  if (!resp.ok) {
    const text = await resp.text().catch(() => "");
    throw new Error(`MailerLite ${resp.status}: ${text.slice(0, 200)}`);
  }
  return resp.json();
}

export async function handler(event) {
  if (event.httpMethod !== "POST") {
    return jsonResponse(405, { success: false, error: "Method not allowed" });
  }

  const ip =
    event.headers["x-nf-client-connection-ip"] ||
    event.headers["x-forwarded-for"]?.split(",")[0]?.trim() ||
    "unknown";

  if (!rateLimitCheck(ip)) {
    return jsonResponse(429, { success: false, error: "Too many requests. Please try again in a few minutes." });
  }

  let payload;
  try {
    payload = JSON.parse(event.body || "{}");
  } catch {
    return jsonResponse(400, { success: false, error: "Invalid request body" });
  }

  const { email, firstName, lastName, company, jobTitle, interests, consent, company_url } = payload;

  if (company_url) {
    return jsonResponse(400, { success: false, error: "Submission blocked" });
  }
  if (!emailValid(email)) {
    return jsonResponse(400, { success: false, error: "Please enter a valid email address." });
  }
  if (consent !== true) {
    return jsonResponse(400, { success: false, error: "Consent is required." });
  }
  if (typeof firstName !== "string" || !firstName.trim()) {
    return jsonResponse(400, { success: false, error: "First name is required." });
  }
  if (firstName.length > 80) {
    return jsonResponse(400, { success: false, error: "First name is too long." });
  }
  if (typeof lastName !== "string" || !lastName.trim()) {
    return jsonResponse(400, { success: false, error: "Last name is required." });
  }
  if (lastName.length > 80) {
    return jsonResponse(400, { success: false, error: "Last name is too long." });
  }
  if (company && (typeof company !== "string" || company.length > 120)) {
    return jsonResponse(400, { success: false, error: "Company is too long." });
  }
  if (jobTitle && (typeof jobTitle !== "string" || jobTitle.length > 120)) {
    return jsonResponse(400, { success: false, error: "Job title is too long." });
  }

  const cleanInterests = Array.isArray(interests)
    ? interests.filter((slug) => INTEREST_SLUGS.includes(slug))
    : [];

  const cleanEmail = email.trim().toLowerCase();
  const cleanFirstName = firstName.trim().slice(0, 80);
  const cleanLastName = lastName.trim().slice(0, 80);
  const cleanCompany = company && typeof company === "string" ? company.trim().slice(0, 120) : undefined;
  const cleanJobTitle = jobTitle && typeof jobTitle === "string" ? jobTitle.trim().slice(0, 120) : undefined;

  let urls;
  try {
    urls = await presignAll();
  } catch (err) {
    console.error("Scaleway presign failed:", err.message || err);
    return jsonResponse(502, { success: false, error: "Could not generate download links. Please try again." });
  }

  try {
    await pushToMailerLite({
      email: cleanEmail,
      firstName: cleanFirstName,
      lastName: cleanLastName,
      company: cleanCompany,
      jobTitle: cleanJobTitle,
      interests: cleanInterests,
      ip,
    });
  } catch (err) {
    console.error("MailerLite push failed:", err.message || err);
    return jsonResponse(502, { success: false, error: "Could not register email. Please try again." });
  }

  return jsonResponse(200, {
    success: true,
    urls,
    expiresIn: URL_TTL_SECONDS,
  });
}
