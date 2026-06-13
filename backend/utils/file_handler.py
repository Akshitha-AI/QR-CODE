from __future__ import annotations

import json
from pathlib import Path

from models.qr_model import QRHistoryItem


def ensure_storage(generated_dir: Path, history_file: Path) -> None:
    generated_dir.mkdir(parents=True, exist_ok=True)
    history_file.parent.mkdir(parents=True, exist_ok=True)
    if not history_file.exists():
        history_file.write_text("[]", encoding="utf-8")


def load_history(history_file: Path) -> list[dict]:
    if not history_file.exists():
        return []
    try:
        data = json.loads(history_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    return data if isinstance(data, list) else []


def append_history(history_file: Path, item: QRHistoryItem) -> None:
    history = load_history(history_file)
    history.insert(0, item.to_dict())
    history_file.write_text(json.dumps(history[:100], indent=2), encoding="utf-8")
