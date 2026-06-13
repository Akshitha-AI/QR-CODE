# Design

## Architecture

The application is a Flask monolith serving both static frontend assets and REST endpoints.

## Components

- Browser UI: form rendering, client validation, preview, history table.
- Flask routes: request handling and JSON responses.
- QR service: content formatting and PNG generation.
- Validator: type-specific validation rules.
- File handler: local JSON history storage.

## Data Flow

User input -> frontend validation -> `/generate` -> backend validation -> QR generation -> history write -> response -> preview and download.

## Sequence Diagram

```text
User -> Frontend: submit form
Frontend -> API: POST /generate
API -> Validator: validate payload
API -> QR Service: generate PNG
API -> History Store: append record
API -> Frontend: QR id and download URL
Frontend -> API: GET /download/<id>
API -> Frontend: PNG
```
