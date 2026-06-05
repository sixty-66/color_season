import type { AnalysisResult } from "./types";
import { mockResult } from "./mockResult";

export async function analyzeColorSeason(
  description: string,
  photo: File | null
): Promise<AnalysisResult> {
  if (window.location.protocol === "file:") {
    await new Promise((resolve) => window.setTimeout(resolve, 520));
    return mockResult;
  }

  const formData = new FormData();
  if (description.trim()) {
    formData.append("description", description.trim());
  }
  if (photo) {
    formData.append("photo", photo);
  }

  const response = await fetch("/api/analyze", {
    method: "POST",
    body: formData
  });

  if (!response.ok) {
    const payload = (await response.json().catch(() => null)) as { detail?: string } | null;
    throw new Error(payload?.detail ?? "分析失败，请稍后重试。");
  }

  return response.json() as Promise<AnalysisResult>;
}
