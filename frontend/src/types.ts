export type Season16Code =
  | "light_spring"
  | "warm_spring"
  | "true_spring"
  | "bright_spring"
  | "light_summer"
  | "soft_summer"
  | "true_summer"
  | "cool_summer"
  | "soft_autumn"
  | "warm_autumn"
  | "true_autumn"
  | "deep_autumn"
  | "deep_winter"
  | "cool_winter"
  | "true_winter"
  | "bright_winter";

export type Season4 = "春季" | "夏季" | "秋季" | "冬季";

export interface SeasonLabel {
  code: Season16Code;
  name_zh: string;
  parent_4: Season4;
  summary: string;
}

export interface PaletteColor {
  name: string;
  hex: string;
  usage: string;
}

export interface AnalysisResult {
  primary_season_4: Season4;
  advanced_season_16: SeasonLabel;
  confidence: number;
  dimensions: {
    undertone: "冷" | "偏冷" | "中性" | "偏暖" | "暖";
    value: "浅" | "中浅" | "中等" | "中深" | "深";
    chroma: "柔和" | "中等" | "清透" | "明亮";
    contrast: "低" | "中低" | "中等" | "中高" | "高";
  };
  evidence: string[];
  sister_seasons: Season16Code[];
  recommendations: {
    neutrals: PaletteColor[];
    accents: PaletteColor[];
    metals: string[];
    outfits: string[];
    makeup: string[];
    avoid: string[];
  };
  photo_quality_notes: string[];
  disclaimer: string;
}
