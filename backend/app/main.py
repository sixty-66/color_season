from fastapi import Depends, FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from backend.app.config import Settings, get_settings
from backend.app.mock_data import MOCK_ANALYSIS
from backend.app.models import AnalysisResult
from backend.app.openai_client import ColorAnalysisClient
from backend.app.validators import (
    ensure_input_present,
    normalize_description,
    read_optional_image,
)


app = FastAPI(
    title="Chromatique 16 API",
    description="面向亚洲用户的四季/16季 AI 色彩分析 API。",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health(settings: Settings = Depends(get_settings)) -> dict[str, str | bool]:
    return {
        "status": "ok",
        "model": settings.openai_model,
        "mock_enabled": settings.allow_mock_analysis,
    }


@app.post("/api/analyze", response_model=AnalysisResult)
async def analyze(
    description: str | None = Form(default=None),
    photo: UploadFile | None = File(default=None),
    settings: Settings = Depends(get_settings),
) -> AnalysisResult:
    normalized = normalize_description(description)
    image_content, image_mime = await read_optional_image(photo, settings.max_image_mb)
    ensure_input_present(normalized, image_content)

    if settings.allow_mock_analysis:
        return MOCK_ANALYSIS

    try:
        return ColorAnalysisClient(settings).analyze(normalized, image_content, image_mime)
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"AI 分析失败：{exc}") from exc

