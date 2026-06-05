import base64
import json

from openai import OpenAI

from backend.app.config import Settings
from backend.app.models import AnalysisResult
from backend.app.prompt import DEVELOPER_PROMPT, build_user_prompt


def encode_image_data_url(content: bytes, mime_type: str) -> str:
    encoded = base64.b64encode(content).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


class ColorAnalysisClient:
    def __init__(self, settings: Settings):
        if not settings.openai_api_key:
            raise RuntimeError("缺少 OPENAI_API_KEY，请在 .env 中配置 OpenAI Platform API key。")
        self.settings = settings
        self.client = OpenAI(
            api_key=settings.openai_api_key,
            timeout=settings.openai_timeout_seconds,
        )

    def analyze(
        self,
        description: str | None,
        image_content: bytes | None,
        image_mime: str | None,
    ) -> AnalysisResult:
        content: list[dict[str, str]] = [
            {"type": "input_text", "text": build_user_prompt(description, bool(image_content))}
        ]
        if image_content and image_mime:
            content.append(
                {
                    "type": "input_image",
                    "image_url": encode_image_data_url(image_content, image_mime),
                }
            )

        response = self.client.responses.create(
            model=self.settings.openai_model,
            instructions=DEVELOPER_PROMPT,
            input=[{"role": "user", "content": content}],
            text={
                "format": {
                    "type": "json_schema",
                    "name": "seasonal_color_analysis",
                    "strict": True,
                    "schema": AnalysisResult.model_json_schema(),
                }
            },
        )
        return AnalysisResult.model_validate(json.loads(response.output_text))

