from __future__ import annotations
from pathlib import Path
from flask import Flask, send_from_directory
from flask_cors import CORS
from config import Config, GENERATED_DIR, HISTORY_FILE
from routes.qr_routes import qr_bp
from utils.file_handler import ensure_storage

FRONTEND_DIR = Path(__file__).resolve().parents[1] / "frontend"
SRC_DIR = Path(__file__).resolve().parents[1]
LIB_DIR = SRC_DIR / "lib"
COMPONENTS_DIR = SRC_DIR / "components"

def create_app() -> Flask:
    app = Flask(__name__, static_folder=str(FRONTEND_DIR), static_url_path="")
    app.config.from_object(Config)
    CORS(app)
    ensure_storage(GENERATED_DIR, HISTORY_FILE)
    app.register_blueprint(qr_bp)

    @app.get("/")
    def index():
        return send_from_directory(FRONTEND_DIR, "index.html")

    @app.get("/lib/<path:filename>")
    def lib_file(filename: str):
        return send_from_directory(LIB_DIR, filename)

    @app.get("/components/<path:filename>")
    def component_file(filename: str):
        return send_from_directory(COMPONENTS_DIR, filename)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=False)
