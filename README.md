# QR Code Generator System

A production-ready Flask web application for creating, previewing, downloading, and tracking QR codes for common data types.

## Problem Statement

Users often need QR codes for links, contact cards, Wi-Fi access, payment IDs, events, and messages. This project provides one responsive web interface and a simple REST API for generating those QR codes.

## Features

- Generate QR codes for text, URLs, contacts, addresses, email, phone, SMS, Wi-Fi, UPI payments, and events.
- Preview generated QR codes in the browser.
- Download generated QR codes as PNG files.
- Validate input on both frontend and backend.
- Store recent generation history in `data/history.json`.
- Include sample CSV and JSON datasets with 100 realistic records.
- Ship with pytest tests, Docker support, and complete documentation.

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/backend/app.py
```

Open `http://127.0.0.1:5000`.

## API Endpoints

- `POST /generate` creates a QR code.
- `GET /download/<id>` returns the generated PNG.
- `GET /history` returns recent generations.
- `GET /health` returns service health.

Example:

```json
{
  "type": "url",
  "content": "https://example.com"
}
```

## Testing

```bash
pytest --cov=src/backend tests
```

## Folder Structure

- `.specify/specs/qr-code-generator` - requirements, design, tasks, and acceptance criteria.
- `docs` - user, API, architecture, installation, and contribution docs.
- `src/frontend` - HTML, CSS, and JavaScript UI.
- `src/backend` - Flask app, routes, services, validators, and models.
- `tests` - pytest coverage for API, validation, and QR generation.
- `assets/sample_dataset` - demo CSV and JSON records.

## Future Scope

- User accounts and per-user history.
- Configurable QR colors and logo overlays.
- Cloud storage for generated images.
- Batch generation from uploaded CSV files.
