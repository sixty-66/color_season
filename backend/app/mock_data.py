from backend.app.models import AnalysisResult


MOCK_ANALYSIS = AnalysisResult.model_validate(
    {
        "primary_season_4": "秋季",
        "advanced_season_16": {
            "code": "deep_autumn",
            "name_zh": "深秋",
            "parent_4": "秋季",
            "summary": "温暖深邃、带一点沉稳清晰感的亚洲深秋型",
        },
        "confidence": 0.78,
        "dimensions": {
            "undertone": "偏暖",
            "value": "中深",
            "chroma": "中等",
            "contrast": "中高",
        },
        "evidence": [
            "整体更适合带棕调、橄榄调和焦糖感的颜色。",
            "过冷的灰粉或冰蓝容易让气色显得发灰。",
            "深色中性色比轻浅粉彩更能托住五官量感。",
        ],
        "sister_seasons": ["warm_autumn", "deep_winter"],
        "recommendations": {
            "neutrals": [
                {"name": "浓咖啡", "hex": "#3B2418", "usage": "大衣、皮具、眼线"},
                {"name": "暖炭灰", "hex": "#4A4038", "usage": "西装、针织"},
                {"name": "橄榄褐", "hex": "#68613D", "usage": "风衣、半裙"},
            ],
            "accents": [
                {"name": "铁锈红", "hex": "#9A3E2E", "usage": "口红、丝巾"},
                {"name": "南瓜橘", "hex": "#B7652A", "usage": "毛衣、腮红"},
                {"name": "深孔雀绿", "hex": "#0E5A50", "usage": "连衣裙、耳饰"},
                {"name": "古金色", "hex": "#B08A3C", "usage": "金属配饰"},
            ],
            "metals": ["古金", "暖玫瑰金", "做旧铜"],
            "outfits": [
                "浓咖啡西装配奶油米内搭，加入古金耳饰。",
                "橄榄褐风衣配铁锈红唇色，适合通勤后约会。",
                "深孔雀绿针织配暖炭灰半裙，气质稳而不暗。",
            ],
            "makeup": [
                "底妆保留自然暖调，不追求过粉白。",
                "眼影选焦糖、可可、橄榄棕，避免银灰珠光。",
                "唇颊适合砖红、豆沙棕、南瓜奶茶色。",
            ],
            "avoid": ["冰粉色", "荧光蓝紫", "纯黑白强对比大面积贴脸"],
        },
        "photo_quality_notes": ["这是 mock 示例；真实分析会根据照片光线与描述调整。"],
        "disclaimer": "色彩分析是穿搭与妆容建议，不代表医学、身份或绝对审美判断。",
    }
)
