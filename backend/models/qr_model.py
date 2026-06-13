from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class QRHistoryItem:
    qr_id: str
    qr_type: str
    title: str
    content: str
    filename: str
    download_url: str
    created_at: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)
