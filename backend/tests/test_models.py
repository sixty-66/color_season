import pytest
from pydantic import ValidationError

from backend.app.mock_data import MOCK_ANALYSIS
from backend.app.models import Season16Code


def test_mock_analysis_has_valid_16_season_parent() -> None:
    assert MOCK_ANALYSIS.advanced_season_16.code == Season16Code.deep_autumn
    assert MOCK_ANALYSIS.advanced_season_16.name_zh == "深秋"
    assert MOCK_ANALYSIS.primary_season_4 == MOCK_ANALYSIS.advanced_season_16.parent_4


def test_invalid_16_season_parent_is_rejected() -> None:
    data = MOCK_ANALYSIS.model_dump(mode="json")
    data["advanced_season_16"]["parent_4"] = "冬季"

    with pytest.raises(ValidationError):
        MOCK_ANALYSIS.__class__.model_validate(data)
