import { useEffect, useMemo, useState } from "react";
import { Droplets, ShieldCheck, Sparkles, SunMedium } from "lucide-react";

import { analyzeColorSeason } from "./api";
import { AnalyzerForm } from "./components/AnalyzerForm";
import { ParticleField } from "./components/ParticleField";
import { ResultReport } from "./components/ResultReport";
import type { AnalysisResult } from "./types";

function App() {
  const [description, setDescription] = useState("");
  const [photo, setPhoto] = useState<File | null>(null);
  const [result, setResult] = useState<AnalysisResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const previewUrl = useMemo(() => {
    if (!photo) {
      return null;
    }
    return URL.createObjectURL(photo);
  }, [photo]);

  useEffect(() => {
    return () => {
      if (previewUrl) {
        URL.revokeObjectURL(previewUrl);
      }
    };
  }, [previewUrl]);

  const handleSubmit = async () => {
    if (!photo && !description.trim()) {
      setError("请上传照片或填写一段个人特征描述。");
      return;
    }
    setLoading(true);
    setError(null);
    try {
      const analysis = await analyzeColorSeason(description, photo);
      setResult(analysis);
    } catch (err) {
      setError(err instanceof Error ? err.message : "分析失败，请稍后重试。");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="app-shell">
      <ParticleField />
      <section className="atelier-layout">
        <aside className="intro-panel reveal">
          <span className="eyebrow">Chromatique 16</span>
          <h1>找到让你气色变干净的颜色</h1>
          <p>
            有些颜色一上身，人会显得轻松；有些颜色明明好看，贴近脸却容易累。
            这里会把你的日常照片或描述整理成四季和 16 季色彩建议。
          </p>
          <div className="daily-notes">
            <span>
              <SunMedium size={16} aria-hidden="true" />
              自然光更准
            </span>
            <span>
              <Droplets size={16} aria-hidden="true" />
              看气色，不看滤镜
            </span>
            <span>
              <ShieldCheck size={16} aria-hidden="true" />
              照片不落盘
            </span>
          </div>
          <div className="color-ribbon" aria-hidden="true">
            <span style={{ background: "#d7efe9" }} />
            <span style={{ background: "#f4d7d2" }} />
            <span style={{ background: "#f7edc9" }} />
            <span style={{ background: "#b7d9f3" }} />
            <span style={{ background: "#c8c0e8" }} />
          </div>
        </aside>
        <AnalyzerForm
          description={description}
          error={error}
          loading={loading}
          photo={photo}
          previewUrl={previewUrl}
          onDescriptionChange={setDescription}
          onPhotoChange={setPhoto}
          onSubmit={handleSubmit}
        />
        {result ? (
          <ResultReport result={result} />
        ) : (
          <aside className="waiting-panel reveal">
            <span className="eyebrow">等一份日常可用的答案</span>
            <h2>结果不是给你贴标签，是帮你少走弯路。</h2>
            <p>
              你会看到适合贴脸的中性色、口红和腮红方向、可以放心买的衣服颜色，
              还有那些最好别大面积靠近脸的颜色。
            </p>
            <div className="season-samples">
              {["浅春", "柔夏", "深秋", "明亮冬"].map((item, index) => (
                <span className={`sample sample-${index + 1}`} key={item}>
                  {item}
                </span>
              ))}
            </div>
          </aside>
        )}
      </section>
    </main>
  );
}

export default App;
