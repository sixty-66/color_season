from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


ROOT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")


class Settings(BaseSettings):
    openai_api_key: str | None = Field(default=None, alias="OPENAI_API_KEY")
    openai_model: str = Field(default="gpt-5.4-mini", alias="OPENAI_MODEL")
    openai_timeout_seconds: int = Field(default=45, alias="OPENAI_TIMEOUT_SECONDS")
    max_image_mb: int = Field(default=8, alias="MAX_IMAGE_MB")
    allow_mock_analysis: bool = Field(default=False, alias="ALLOW_MOCK_ANALYSIS")

    model_config = SettingsConfigDict(extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()

