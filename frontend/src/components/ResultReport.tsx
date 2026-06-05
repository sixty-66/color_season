import { Check, Gem, Palette, Shirt, Sparkle, Wand2 } from "lucide-react";

import { season16Names, seasonMood } from "../seasonNames";
import type { AnalysisResult, PaletteColor, Season16Code } from "../types";

interface ResultReportProps {
  result: AnalysisResult;
}

function ColorSwatch({ color }: { color: PaletteColor }) {
  return (
    <div className="swatch">
      <span className="swatch-chip" style={{ background: color.hex }} />
      <div>
        <strong>{color.name}</strong>
        <small>{color.usage}</small>
      </div>
    </div>
  );
}

function DimensionBar({ label, value }: { label: string; value: string }) {
  return (
    <div className="dimension-row">
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  );
}

function SeasonPill({ code }: { code: Season16Code }) {
  return <span className="season-pill">{season16Names[code]}</span>;
}

export function ResultReport({ result }: ResultReportProps) {
  const seasonCode = result.advanced_season_16.code;
  const confidence = Math.round(result.confidence * 100);

  return (
    <section className="report reveal">
      <div className="report-hero">
        <div>
          <span className="eyebrow">你的色彩方向</span>
          <h2>
            {result.primary_season_4} / {season16Names[seasonCode]}
          </h2>
          <p>{result.advanced_season_16.summary || seasonMood[seasonCode]}</p>
        </div>
        <div className="confidence-ring" aria-label={`置信度 ${confidence}%`}>
          <span>{confidence}%</span>
          <small>资料完整度</small>
        </div>
      </div>

      <div className="report-grid">
        <div className="report-block">
          <h3>
            <Palette aria-hidden="true" />
            怎么看出来的
          </h3>
          <DimensionBar label="冷暖" value={result.dimensions.undertone} />
          <DimensionBar label="明度" value={result.dimensions.value} />
          <DimensionBar label="彩度" value={result.dimensions.chroma} />
          <DimensionBar label="对比度" value={result.dimensions.contrast} />
        </div>

        <div className="report-block">
          <h3>
            <Check aria-hidden="true" />
            贴近生活的线索
          </h3>
          <ul className="clean-list">
            {result.evidence.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
      </div>

      <div className="palette-section">
        <div className="section-title">
          <Gem aria-hidden="true" />
          <h3>可以先试这些颜色</h3>
        </div>
        <div className="swatch-grid">
          {[...result.recommendations.neutrals, ...result.recommendations.accents].map((color) => (
            <ColorSwatch color={color} key={`${color.name}-${color.hex}`} />
          ))}
        </div>
      </div>

      <div className="recommendation-grid">
        <div className="report-block">
          <h3>
            <Shirt aria-hidden="true" />
            衣柜可以这样选
          </h3>
          <ul className="clean-list">
            {result.recommendations.outfits.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>

        <div className="report-block">
          <h3>
            <Wand2 aria-hidden="true" />
            妆面不用太用力
          </h3>
          <ul className="clean-list">
            {result.recommendations.makeup.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
      </div>

      <div className="notes-row">
        <div>
          <h3>
            <Sparkle aria-hidden="true" />
            也可以借一点
          </h3>
          <div className="pill-row">
            {result.sister_seasons.map((code) => (
              <SeasonPill code={code} key={code} />
            ))}
          </div>
        </div>
        <div>
          <h3>先少大面积贴脸</h3>
          <div className="avoid-row">
            {result.recommendations.avoid.map((item) => (
              <span key={item}>{item}</span>
            ))}
          </div>
        </div>
      </div>

      <p className="disclaimer">{result.disclaimer}</p>
      <p className="quality-note">{result.photo_quality_notes.join(" ")}</p>
    </section>
  );
}
