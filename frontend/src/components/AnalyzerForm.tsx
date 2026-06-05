import { Camera, Loader2, Sparkles, Upload, X } from "lucide-react";
import type { FormEvent } from "react";

interface AnalyzerFormProps {
  description: string;
  photo: File | null;
  previewUrl: string | null;
  loading: boolean;
  error: string | null;
  onDescriptionChange: (value: string) => void;
  onPhotoChange: (file: File | null) => void;
  onSubmit: () => void;
}

export function AnalyzerForm({
  description,
  photo,
  previewUrl,
  loading,
  error,
  onDescriptionChange,
  onPhotoChange,
  onSubmit
}: AnalyzerFormProps) {
  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    onSubmit();
  };

  return (
    <form className="studio-panel reveal" onSubmit={handleSubmit}>
      <div className="panel-header">
        <span className="eyebrow">先从真实的你开始</span>
        <h2>放一张平时的照片，或写几句你的穿衣感受</h2>
        <p>素颜、淡妆都可以。重点是光线干净，别让滤镜替你决定肤色。</p>
      </div>

      <label className="upload-zone">
        <input
          accept="image/png,image/jpeg,image/webp"
          type="file"
          onChange={(event) => onPhotoChange(event.target.files?.[0] ?? null)}
        />
        {previewUrl ? (
          <img className="preview-image" src={previewUrl} alt="上传预览" />
        ) : (
          <div className="upload-empty">
            <Camera aria-hidden="true" />
            <strong>放一张日常照片</strong>
            <span>窗边光、少修图、能看到发色和眼睛就很好</span>
          </div>
        )}
        <span className="upload-action">
          <Upload size={16} aria-hidden="true" />
          {photo ? photo.name : "选择一张照片"}
        </span>
      </label>

      {photo && (
        <button className="text-button" type="button" onClick={() => onPhotoChange(null)}>
          <X size={16} aria-hidden="true" />
          移除照片
        </button>
      )}

      <label className="field">
        <span>也可以补充你的直觉</span>
        <textarea
          placeholder="比如：自然黑发，棕黑眼睛。穿冷粉会显灰，橄榄绿和砖红比较有精神；纯黑贴脸有点重。"
          value={description}
          onChange={(event) => onDescriptionChange(event.target.value)}
        />
      </label>

      {error && <p className="error-message">{error}</p>}

      <button className="primary-button" disabled={loading} type="submit">
        {loading ? <Loader2 className="spin" aria-hidden="true" /> : <Sparkles aria-hidden="true" />}
        {loading ? "正在整理你的色彩线索" : "看看适合我的颜色"}
      </button>
    </form>
  );
}
