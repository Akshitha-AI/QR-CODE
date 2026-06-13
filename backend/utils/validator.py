from __future__ import annotations

import re
from datetime import datetime
from urllib.parse import urlparse


SUPPORTED_TYPES = {
    "text",
    "url",
    "contact",
    "address",
    "email",
    "phone",
    "sms",
    "wifi",
    "upi",
    "event",
}

EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
PHONE_PATTERN = re.compile(r"^\+?[0-9][0-9\s().-]{7,18}$")
UPI_PATTERN = re.compile(r"^[A-Za-z0-9.\-_]{2,256}@[A-Za-z]{2,64}$")


def validate_payload(payload: dict | None) -> tuple[bool, str]:
    if not isinstance(payload, dict):
        return False, "Request body must be a JSON object."

    qr_type = str(payload.get("type", "")).strip().lower()
    content = payload.get("content")

    if qr_type not in SUPPORTED_TYPES:
        return False, f"Unsupported QR type. Use one of: {', '.join(sorted(SUPPORTED_TYPES))}."
    if content is None:
        return False, "Content is required."
    if isinstance(content, dict):
        return _validate_structured(qr_type, content)

    text = str(content).strip()
    if not text:
        return False, "Content cannot be empty."

    validators = {
        "url": _is_valid_url,
        "email": _is_valid_email,
        "phone": _is_valid_phone,
        "upi": _is_valid_upi,
    }
    validator = validators.get(qr_type)
    if validator and not validator(text):
        return False, f"Invalid {qr_type} content."
    return True, ""


def _validate_structured(qr_type: str, content: dict) -> tuple[bool, str]:
    required_fields = {
        "contact": ["name", "phone"],
        "wifi": ["ssid", "password"],
        "sms": ["phone", "message"],
        "event": ["title", "start"],
    }
    for field in required_fields.get(qr_type, []):
        if not str(content.get(field, "")).strip():
            return False, f"{field} is required for {qr_type} QR codes."

    phone = content.get("phone")
    email = content.get("email")
    upi_id = content.get("upi_id")
    start = content.get("start")

    if phone and not _is_valid_phone(str(phone)):
        return False, "Invalid phone number."
    if email and not _is_valid_email(str(email)):
        return False, "Invalid email address."
    if upi_id and not _is_valid_upi(str(upi_id)):
        return False, "Invalid UPI ID."
    if qr_type == "event" and start:
        try:
            datetime.fromisoformat(str(start).replace("Z", "+00:00"))
        except ValueError:
            return False, "Event start must be an ISO date/time."
    return True, ""


def _is_valid_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def _is_valid_email(value: str) -> bool:
    return bool(EMAIL_PATTERN.fullmatch(value.strip()))


def _is_valid_phone(value: str) -> bool:
    return bool(PHONE_PATTERN.fullmatch(value.strip()))


def _is_valid_upi(value: str) -> bool:
    return bool(UPI_PATTERN.fullmatch(value.strip()))
