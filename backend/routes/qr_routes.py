from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from flask import Blueprint, current_app, jsonify, request, send_from_directory

from config import GENERATED_DIR, HISTORY_FILE
from models.qr_model import QRHistoryItem
from services.qr_generator import build_qr_content, generate_qr_image
from utils.file_handler import append_history, ensure_storage, load_history
from utils.validator import validate_payload

qr_bp = Blueprint("qr", __name__)


@qr_bp.post("/generate")
def generate() -> tuple:
    payload = request.get_json(silent=True)
    is_valid, error = validate_payload(payload)
    if not is_valid:
        return jsonify({"success": False, "error": error}), 400

    qr_id = str(uuid4())
    qr_type = str(payload["type"]).strip().lower()
    filename = f"{qr_id}.png"
    output_path = GENERATED_DIR / filename
    ensure_storage(GENERATED_DIR, HISTORY_FILE)

    qr_content = build_qr_content(qr_type, payload["content"])
    generate_qr_image(qr_content, output_path)

    item = QRHistoryItem(
        qr_id=qr_id,
        qr_type=qr_type,
        title=str(payload.get("title") or qr_type.title()),
        content=qr_content,
        filename=filename,
        download_url=f"/download/{qr_id}",
        created_at=datetime.now(timezone.utc).isoformat(),
    )
    append_history(HISTORY_FILE, item)

    return jsonify(
        {
            "success": True,
            "qr_id": qr_id,
            "download_url": item.download_url,
            "preview_url": item.download_url,
        }
    ), 201


@qr_bp.get("/download/<qr_id>")
def download(qr_id: str):
    filename = f"{qr_id}.png"
    file_path = GENERATED_DIR / filename
    if not file_path.exists():
        return jsonify({"success": False, "error": "QR code not found."}), 404
    return send_from_directory(Path(GENERATED_DIR), filename, mimetype="image/png", as_attachment=True)


@qr_bp.get("/history")
def history() -> tuple:
    ensure_storage(GENERATED_DIR, HISTORY_FILE)
    return jsonify({"success": True, "items": load_history(HISTORY_FILE)}), 200


@qr_bp.get("/health")
def health() -> tuple:
    return jsonify({"success": True, "status": "healthy", "service": current_app.name}), 200
