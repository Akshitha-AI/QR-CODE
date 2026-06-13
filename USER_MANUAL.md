# QR Code Generator - User Manual

Welcome to the QR Code Generator! This manual will guide you through using all features of the application.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Features](#features)
- [Web Interface](#web-interface)
- [API Usage](#api-usage)
- [Advanced Configuration](#advanced-configuration)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)

## Installation

### Option 1: Using Docker (Recommended)

```bash
docker-compose up -d
```

Access the application at `http://localhost:5000`

### Option 2: Manual Installation

**Requirements:**
- Python 3.8+
- pip

**Steps:**

1. Clone the repository:
   ```bash
   git clone https://gitlab.com/surakanti-akshitha/qr-code.git
   cd qr-code
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python src/backend/app.py
   ```

5. Access at `http://localhost:5000`

## Quick Start

### Generate a Simple QR Code

1. Open the web interface at `http://localhost:5000`
2. Enter your data in the text field (URL, text, contact info, etc.)
3. Click "Generate QR Code"
4. Download the generated image

### Batch Processing

1. Go to "Batch Processing" tab
2. Upload a CSV or JSON file with data
3. Configure QR code options
4. Click "Process Batch"
5. Download the ZIP file with all generated codes

## Features

### Basic QR Code Generation

- **Text to QR:** Convert any text to QR code
- **URL Encoding:** Automatically optimizes URLs
- **Contact Cards:** Generate vCard/vCal formats
- **WiFi Codes:** Create WiFi connection codes

### Customization

- **Size Options:** Small (21x21) to XXL (177x177)
- **Error Correction:** L, M, Q, H levels (15-30% recovery)
- **Colors:** Custom foreground/background colors
- **Logo Embedding:** Add your logo to the center
- **Formats:** PNG, SVG, PDF output

### Batch Processing

- Process multiple QR codes from CSV/JSON
- Maintain data history
- Download as ZIP archive
- Track processing status

### History

- View previously generated QR codes
- Re-download any past generation
- Export history as CSV
- Clear history (irreversible)

## Web Interface

### Main Page

```
┌─────────────────────────────────────┐
│     QR Code Generator               │
├─────────────────────────────────────┤
│                                     │
│  [Data Input Field]                 │
│  [Generate] [Download] [Reset]      │
│                                     │
│  Preview of Generated QR Code       │
│                                     │
└─────────────────────────────────────┘
```

### Top Navigation

- **Home** - Main generation interface
- **Batch** - Process multiple QR codes
- **History** - View past generations
- **Settings** - Configure defaults
- **API Docs** - View API endpoints

### Settings Panel

**Size:** Choose QR code dimensions
**Error Correction:** Increase data recovery capability
**Color Options:** Set colors for code and background
**Format:** Choose output format (PNG, SVG, PDF)

## API Usage

### Generate Single QR Code

**Endpoint:** `POST /api/generate`

**Request:**
```json
{
  "data": "https://example.com",
  "size": "M",
  "error_correction": "M",
  "format": "png",
  "color": "#000000",
  "background": "#FFFFFF"
}
```

**Response:**
```json
{
  "success": true,
  "qr_code": "base64_encoded_image",
  "metadata": {
    "timestamp": "2024-01-15T10:30:00",
    "id": "qr_123456"
  }
}
```

### Batch Generate

**Endpoint:** `POST /api/batch`

**Request:**
```json
{
  "file": "multipart_file",
  "format": "csv",
  "options": {
    "size": "M",
    "error_correction": "M"
  }
}
```

**Response:**
```json
{
  "success": true,
  "batch_id": "batch_123",
  "total": 100,
  "status": "processing"
}
```

### Get History

**Endpoint:** `GET /api/history`

**Response:**
```json
{
  "history": [
    {
      "id": "qr_123",
      "data": "https://example.com",
      "timestamp": "2024-01-15T10:30:00",
      "format": "png"
    }
  ]
}
```

See [API Documentation](docs/API_DOCUMENTATION.md) for complete API reference.

## Advanced Configuration

### Environment Variables

Create a `.env` file (see `.env.example`):

```env
FLASK_ENV=production
DEBUG=False
MAX_FILE_SIZE=10MB
BATCH_TIMEOUT=300
LOG_LEVEL=INFO
```

### Custom Themes

Edit `src/frontend/css/style.css` to customize appearance.

### Data Validation

The application validates:
- Maximum data length (2953 bytes for QR code)
- Valid URLs and email formats
- File size limits for batch processing

## Troubleshooting

### QR Code Not Generating

**Solution:**
1. Check if data exceeds 2953 bytes
2. Verify special characters are encoded correctly
3. Try reducing error correction level

### Batch Processing Timeout

**Solution:**
1. Reduce file size
2. Split into multiple batches
3. Increase `BATCH_TIMEOUT` environment variable

### Download Issues

**Solution:**
1. Disable browser privacy extensions
2. Check browser download settings
3. Ensure sufficient disk space

### Docker Container Won't Start

**Solution:**
```bash
# Check logs
docker-compose logs -f

# Rebuild
docker-compose down
docker-compose up --build
```

## FAQ

### Q: What's the maximum data length?
**A:** 2953 bytes. Longer data requires higher version QR codes or multiple codes.

### Q: Can I embed images in QR codes?
**A:** Yes! Use the logo upload feature to add your logo to the center.

### Q: Are my QR codes stored?
**A:** Temporarily in the `generated/` folder and in browser history. Enable "Privacy Mode" to disable storage.

### Q: What formats are supported?
**A:** PNG (raster), SVG (vector), PDF (document).

### Q: Can I batch generate?
**A:** Yes! Upload CSV/JSON with data and process multiple codes at once.

### Q: Is there an API?
**A:** Yes! See the [API Documentation](docs/API_DOCUMENTATION.md).

### Q: How do I contribute?
**A:** See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Q: What license is this?
**A:** AGPL-3.0. See [LICENSE](LICENSE) for details.

---

**Need help?** Open an issue or check the [Contributing Guide](CONTRIBUTING.md).
