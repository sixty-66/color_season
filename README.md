# 亚洲用户导向四季/16季色彩 AI 测试

本项目是一个本地 MVP：上传个人照片或描述个人特征后，由后端调用 OpenAI 视觉模型，生成中文 4 季主判断、16 季进阶判断、穿搭色系、妆容色系和避雷色。

## 本地运行

### 只看前端界面

最稳的双击预览：

```text
preview.html
```

这个文件是单文件静态预览，不需要 Vite、后端或网络。上传照片只会在浏览器本地显示预览。

如果想看 React/Vite 构建结果：

```bash
npm install
npm run build
```

然后打开 `dist/index.html`。注意：部分浏览器会拦截 `file://` 下的 ES module；遇到空白页时请改用 `preview.html` 或启动 Vite。

### 前后端联调

1. 安装后端依赖：

```bash
conda activate explore_py312
pip install -r requirements.txt
```

2. 配置 API key：

```bash
cp .env.example .env
```

编辑 `.env`，填入 `OPENAI_API_KEY`。ChatGPT Plus 不能直接调用 API；API 使用需要 OpenAI Platform 的 API key 和单独计费。

3. 启动后端：

```bash
conda activate explore_py312
uvicorn backend.app.main:app --reload --port 8000
```

4. 启动前端：

```bash
npm install
npm run dev -- --host 0.0.0.0
```

默认前端访问 `http://localhost:5173`，后端访问 `http://localhost:8000`。

## 隐私与适配说明

- 照片只在请求生命周期内处理，不落盘保存。
- 本产品面向中文与亚洲用户做穿搭/妆容建议，但不会从照片推断种族、国籍或身份。
- 提示词会避免把黑发、深棕瞳自动判定为冬季或深色型，更重视冷暖、明度、彩度、对比度和整体清透/柔和程度。
