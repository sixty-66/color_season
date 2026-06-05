import asyncio

import pytest
from fastapi import HTTPException

from backend.app.config import Settings
from backend.app.main import health
from backend.app.validators import (
    ensure_input_present,
    normalize_description,
    read_optional_image,
)


class StubUpload:
    def __init__(self, content: bytes, content_type: str):
        self._content = content
        self.content_type = content_type

    async def read(self) -> bytes:
        return self._content


def test_health_payload() -> None:
    payload = health(Settings(OPENAI_MODEL="test-model", ALLOW_MOCK_ANALYSIS=True))
    assert payload["status"] == "ok"
    assert payload["model"] == "test-model"
    assert payload["mock_enabled"] is True


def test_analyze_requires_photo_or_description() -> None:
    with pytest.raises(HTTPException) as exc:
        ensure_input_present(None, None)
    assert exc.value.status_code == 400
    assert "请上传照片或填写个人特征描述" in exc.value.detail


def test_normalize_description_trims_blank_text() -> None:
    assert normalize_description("  黑发，橄榄调肤色  ") == "黑发，橄榄调肤色"
    assert normalize_description("   ") is None


def test_rejects_invalid_image_type() -> None:
    upload = StubUpload(b"hello", "text/plain")
    with pytest.raises(HTTPException) as exc:
        asyncio.run(read_optional_image(upload, max_mb=8))  # type: ignore[arg-type]
    assert exc.value.status_code == 400
    assert "仅支持" in exc.value.detail


def test_accepts_valid_image_type() -> None:
    upload = StubUpload(b"image-bytes", "image/png")
    content, mime = asyncio.run(read_optional_image(upload, max_mb=8))  # type: ignore[arg-type]
    assert content == b"image-bytes"
    assert mime == "image/png"

