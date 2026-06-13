from __future__ import annotations

import json
from pathlib import Path
from urllib.error import URLError
from urllib.parse import quote_plus
from urllib.request import Request, urlopen

import qrcode
from PIL import Image


def build_qr_content(qr_type: str, content: str | dict) -> str:
    if not isinstance(content, dict):
        value = str(content).strip()
        if qr_type == "address":
            return _build_openstreetmap_address_url(value)
        return value

    if qr_type == "contact":
        lines = [
            "BEGIN:VCARD",
            "VERSION:3.0",
            f"FN:{content.get('name', '')}",
            f"TEL:{content.get('phone', '')}",
            f"EMAIL:{content.get('email', '')}",
            f"ADR:{content.get('address', '')}",
            "END:VCARD",
        ]
        return "\n".join(line for line in lines if not line.endswith(":"))
    if qr_type == "wifi":
        encryption = content.get("encryption", "WPA")
        hidden = "true" if content.get("hidden") else "false"
        return f"WIFI:T:{encryption};S:{content.get('ssid', '')};P:{content.get('password', '')};H:{hidden};;"
    if qr_type == "sms":
        return f"SMSTO:{content.get('phone', '')}:{content.get('message', '')}"
    if qr_type == "upi":
        return (
            "upi://pay?"
            f"pa={content.get('upi_id', '')}&pn={content.get('name', '')}"
            f"&am={content.get('amount', '')}&cu=INR"
        )
    if qr_type == "event":
        return (
            "BEGIN:VEVENT\n"
            f"SUMMARY:{content.get('title', '')}\n"
            f"DTSTART:{content.get('start', '')}\n"
            f"DTEND:{content.get('end', '')}\n"
            f"LOCATION:{content.get('location', '')}\n"
            f"DESCRIPTION:{content.get('description', '')}\n"
            "END:VEVENT"
        )
    return json.dumps(content, ensure_ascii=True)


def _build_openstreetmap_address_url(address: str) -> str:
    query = quote_plus(address)
    search_url = f"https://www.openstreetmap.org/search?query={query}"
    try:
        coords = _geocode_address(address)
        if coords:
            lat, lon = coords
            return f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=18/{lat}/{lon}"
    except (URLError, ValueError, OSError):
        pass
    return search_url


def _geocode_address(address: str) -> tuple[str, str] | None:
    url = f"https://nominatim.openstreetmap.org/search?format=json&limit=1&q={quote_plus(address)}"
    request = Request(url, headers={"User-Agent": "qr-code-generator-app/1.0"})
    with urlopen(request, timeout=10) as response:
        data = json.load(response)
    if not data or not isinstance(data, list):
        return None
    first = data[0]
    lat = first.get("lat")
    lon = first.get("lon")
    if lat and lon:
        return str(lat), str(lon)
    return None


def generate_qr_image(data: str, output_path: Path) -> None:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color="#111827", back_color="white").convert("RGB")
    branded = _add_padding(image)
    branded.save(output_path, format="PNG", optimize=True)


def _add_padding(image: Image.Image) -> Image.Image:
    padding = 24
    canvas = Image.new("RGB", (image.width + padding * 2, image.height + padding * 2), "white")
    canvas.paste(image, (padding, padding))
    return canvas
