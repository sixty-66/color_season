from fastapi import HTTPException, UploadFile


ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/webp"}


async def read_optional_image(file: UploadFile | None, max_mb: int) -> tuple[bytes | None, str | None]:
    if file is None:
        return None, None
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(status_code=400, detail="仅支持 JPG、PNG 或 WebP 图片。")

    content = await file.read()
    max_bytes = max_mb * 1024 * 1024
    if len(content) > max_bytes:
        raise HTTPException(status_code=400, detail=f"图片不能超过 {max_mb}MB。")
    if not content:
        raise HTTPException(status_code=400, detail="上传的图片为空。")
    return content, file.content_type


def normalize_description(description: str | None) -> str | None:
    if description is None:
        return None
    value = description.strip()
    return value or None


def ensure_input_present(description: str | None, image_content: bytes | None) -> None:
    if not description and not image_content:
        raise HTTPException(status_code=400, detail="请上传照片或填写个人特征描述。")

