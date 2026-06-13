# Acceptance Criteria

- The app starts with `python src/backend/app.py`.
- `/health` returns HTTP 200.
- `/generate` creates PNG QR codes for supported types.
- `/download/<id>` returns `image/png` for generated IDs.
- `/history` returns generated QR records.
- Invalid URLs, emails, phone numbers, and UPI IDs return HTTP 400.
- The frontend is usable on desktop and mobile widths.
- Tests cover API endpoints, validators, and QR generation.
- Sample CSV and JSON datasets contain at least 100 records.
