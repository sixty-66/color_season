import type { AnalysisResult } from "./types";

export const mockResult: AnalysisResult = {
  primary_season_4: "秋季",
  advanced_season_16: {
    code: "deep_autumn",
    name_zh: "深秋",
    parent_4: "秋季",
    summary: "颜色需要有一点厚度和暖意，太冷太轻的颜色容易让脸色发灰。"
  },
  confidence: 0.78,
  dimensions: {
    undertone: "偏暖",
    value: "中深",
    chroma: "中等",
    contrast: "中高"
  },
  evidence: [
    "棕调、橄榄调、焦糖感的颜色更容易把气色托起来。",
    "冷粉、冰蓝和银灰靠近脸时，容易显得疲惫或泛灰。",
    "比起轻浅粉彩，带一点深度的中性色更稳。"
  ],
  sister_seasons: ["warm_autumn", "deep_winter"],
  recommendations: {
    neutrals: [
      { name: "浓咖啡", hex: "#3B2418", usage: "外套、皮具、眼线" },
      { name: "暖炭灰", hex: "#4A4038", usage: "西装、针织" },
      { name: "橄榄褐", hex: "#68613D", usage: "风衣、半裙" }
    ],
    accents: [
      { name: "铁锈红", hex: "#9A3E2E", usage: "口红、丝巾" },
      { name: "南瓜橘", hex: "#B7652A", usage: "毛衣、腮红" },
      { name: "深孔雀绿", hex: "#0E5A50", usage: "连衣裙、耳饰" },
      { name: "古金色", hex: "#B08A3C", usage: "金属配饰" }
    ],
    metals: ["古金", "暖玫瑰金", "做旧铜"],
    outfits: [
      "浓咖啡西装配奶油米内搭，通勤不会太沉。",
      "橄榄褐风衣加铁锈红唇色，适合下班后的约会。",
      "深孔雀绿针织配暖炭灰半裙，看起来稳，但不暗。"
    ],
    makeup: [
      "底妆保留自然暖调，不需要刻意压成粉白。",
      "眼影可以试焦糖、可可、橄榄棕，少用银灰珠光。",
      "唇颊适合砖红、豆沙棕、南瓜奶茶色。"
    ],
    avoid: ["冰粉色", "荧光蓝紫", "纯黑白强对比大面积贴脸"]
  },
  photo_quality_notes: ["这是本地 HTML 预览示例；接入后端后会根据照片和描述重新分析。"],
  disclaimer: "色彩分析是穿搭和妆容建议，不是医学、身份或绝对审美判断。"
};

