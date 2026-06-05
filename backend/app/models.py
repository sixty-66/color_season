from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field, field_validator


class Season4(str, Enum):
    spring = "春季"
    summer = "夏季"
    autumn = "秋季"
    winter = "冬季"


class Season16Code(str, Enum):
    light_spring = "light_spring"
    warm_spring = "warm_spring"
    true_spring = "true_spring"
    bright_spring = "bright_spring"
    light_summer = "light_summer"
    soft_summer = "soft_summer"
    true_summer = "true_summer"
    cool_summer = "cool_summer"
    soft_autumn = "soft_autumn"
    warm_autumn = "warm_autumn"
    true_autumn = "true_autumn"
    deep_autumn = "deep_autumn"
    deep_winter = "deep_winter"
    cool_winter = "cool_winter"
    true_winter = "true_winter"
    bright_winter = "bright_winter"


SEASON_16_NAMES: dict[Season16Code, str] = {
    Season16Code.light_spring: "浅春",
    Season16Code.warm_spring: "暖春",
    Season16Code.true_spring: "正春",
    Season16Code.bright_spring: "明亮春",
    Season16Code.light_summer: "浅夏",
    Season16Code.soft_summer: "柔夏",
    Season16Code.true_summer: "正夏",
    Season16Code.cool_summer: "冷夏",
    Season16Code.soft_autumn: "柔秋",
    Season16Code.warm_autumn: "暖秋",
    Season16Code.true_autumn: "正秋",
    Season16Code.deep_autumn: "深秋",
    Season16Code.deep_winter: "深冬",
    Season16Code.cool_winter: "冷冬",
    Season16Code.true_winter: "正冬",
    Season16Code.bright_winter: "明亮冬",
}


SEASON_16_PARENT: dict[Season16Code, Season4] = {
    Season16Code.light_spring: Season4.spring,
    Season16Code.warm_spring: Season4.spring,
    Season16Code.true_spring: Season4.spring,
    Season16Code.bright_spring: Season4.spring,
    Season16Code.light_summer: Season4.summer,
    Season16Code.soft_summer: Season4.summer,
    Season16Code.true_summer: Season4.summer,
    Season16Code.cool_summer: Season4.summer,
    Season16Code.soft_autumn: Season4.autumn,
    Season16Code.warm_autumn: Season4.autumn,
    Season16Code.true_autumn: Season4.autumn,
    Season16Code.deep_autumn: Season4.autumn,
    Season16Code.deep_winter: Season4.winter,
    Season16Code.cool_winter: Season4.winter,
    Season16Code.true_winter: Season4.winter,
    Season16Code.bright_winter: Season4.winter,
}


class SeasonLabel(BaseModel):
    code: Season16Code
    name_zh: str = Field(min_length=2, max_length=8)
    parent_4: Season4
    summary: str = Field(min_length=6, max_length=80)


class PaletteColor(BaseModel):
    name: str = Field(min_length=1, max_length=24)
    hex: str = Field(pattern=r"^#[0-9A-Fa-f]{6}$")
    usage: str = Field(min_length=2, max_length=50)


class ColorDimension(BaseModel):
    undertone: Literal["冷", "偏冷", "中性", "偏暖", "暖"]
    value: Literal["浅", "中浅", "中等", "中深", "深"]
    chroma: Literal["柔和", "中等", "清透", "明亮"]
    contrast: Literal["低", "中低", "中等", "中高", "高"]


class RecommendationSet(BaseModel):
    neutrals: list[PaletteColor] = Field(min_length=3, max_length=6)
    accents: list[PaletteColor] = Field(min_length=4, max_length=8)
    metals: list[str] = Field(min_length=1, max_length=4)
    outfits: list[str] = Field(min_length=3, max_length=6)
    makeup: list[str] = Field(min_length=3, max_length=6)
    avoid: list[str] = Field(min_length=2, max_length=6)


class AnalysisResult(BaseModel):
    primary_season_4: Season4
    advanced_season_16: SeasonLabel
    confidence: float = Field(ge=0, le=1)
    dimensions: ColorDimension
    evidence: list[str] = Field(min_length=3, max_length=6)
    sister_seasons: list[Season16Code] = Field(min_length=1, max_length=3)
    recommendations: RecommendationSet
    photo_quality_notes: list[str] = Field(min_length=1, max_length=4)
    disclaimer: str = Field(min_length=10, max_length=180)

    @field_validator("advanced_season_16")
    @classmethod
    def validate_parent(cls, label: SeasonLabel) -> SeasonLabel:
        expected_parent = SEASON_16_PARENT[label.code]
        if label.parent_4 != expected_parent:
            raise ValueError("16季 code 与 4季父级不匹配")
        if label.name_zh != SEASON_16_NAMES[label.code]:
            raise ValueError("16季中文名称必须与 code 枚举一致")
        return label


class ApiError(BaseModel):
    detail: str
