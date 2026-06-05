# AGENTS.md

## Project Context

This project is a local MVP for an Asian-user-oriented seasonal color analysis web app. It accepts a personal photo and/or a written feature description, calls the OpenAI API from the backend, and returns a Chinese 4-season plus 16-season color report.

## Run Commands

- Create or update Python dependencies: `conda activate explore_py312` then `pip install -r requirements.txt`.
- Backend dev server: `conda activate explore_py312` then `uvicorn backend.app.main:app --reload --port 8000`.
- Frontend dependencies: `npm install`.
- Frontend dev server: `npm run dev -- --host 0.0.0.0`.
- Static frontend preview: `npm run build`, then open `dist/index.html`; file-protocol preview uses local mock data.
- Double-click preview: open `preview.html`; it is standalone and does not call the backend.
- Backend tests: `conda activate explore_py312` then `pytest backend/tests`.
- Frontend checks: `npm run typecheck` and `npm run build`.

## OpenAI Configuration

- Put `OPENAI_API_KEY` in `.env` at the project root. Never expose it to browser code.
- `OPENAI_MODEL` defaults to `gpt-5.4-mini`; it can be changed in `.env`.
- ChatGPT Plus is a ChatGPT web subscription and does not include API usage. API calls require an OpenAI Platform API key and separate API billing.

## Product Rules

- The product is designed for Chinese-speaking Asian users, especially everyday styling, commute, dating, light mature style, and refined natural makeup contexts.
- The backend prompt must avoid Eurocentric color-analysis bias. Do not classify black hair or dark brown eyes as Winter or deep types by default.
- Treat "Asian user" as product and recommendation context only. Do not infer race, ethnicity, nationality, or identity from a photo.
- Mention that lighting, filters, dyed hair, heavy makeup, and camera white balance may affect the result.

## Code Quality

- Keep files under 500 lines.
- Keep modules focused: API routes, prompt construction, OpenAI client, schemas, validation, and UI components should stay separate.
- Prefer typed schemas and enums over free-form strings.
- Do not store uploaded photos; process them only during the request lifecycle.
- Keep comments short and useful. Avoid broad refactors outside the current task.
