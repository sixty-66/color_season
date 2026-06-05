from backend.app.prompt import DEVELOPER_PROMPT, build_user_prompt


def test_prompt_contains_asian_user_adaptation_rules() -> None:
    assert "面向亚洲用户" in DEVELOPER_PROMPT
    assert "黑发、深色瞳孔" in DEVELOPER_PROMPT
    assert "自动等同于冬季" in DEVELOPER_PROMPT
    assert "不得从照片推断种族" in DEVELOPER_PROMPT


def test_user_prompt_mentions_no_eurocentric_default() -> None:
    prompt = build_user_prompt("黑发，棕黑眼睛，肤色偏橄榄", has_image=False)
    assert "不用欧美浅发浅瞳作为默认参照" in prompt
    assert "用户未上传照片" in prompt
