# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the app

```bash
pip install -r requirements.txt
python app.py
```

The dev server runs at `http://127.0.0.1:5000` with auto-reload enabled (debug mode).

## Deploying

The app is hosted on **Render.com** connected to the GitHub repo `fabiodl77/portfolio-fdl`. Every push to `main` triggers an automatic redeploy.

```bash
git add .
git commit -m "message"
git push
```

Production start command (defined in `render.yaml`): `gunicorn app:app`

## Architecture

Single-file Flask app (`app.py`) with no database. All profile content lives in the `profile` dict at the top of `app.py` — this is the only place to edit personal data (name, experiences, skills, courses, etc.).

- `app.py` — profile data + single route `/` rendering `templates/index.html`
- `templates/index.html` — Jinja2 template; iterates over `profile` dict sections
- `static/css/style.css` — all styles (CSS custom properties in `:root` for theming)
- `static/js/main.js` — navbar scroll effect, active link highlight, IntersectionObserver fade-ins
- `static/foto.png` — profile photo rendered in the hero avatar

## Key data structures in `app.py`

- `profile["experiences"]` — list of dicts with keys: `period`, `role`, `company`, `size`, `description`, `highlights` (list)
- `profile["courses"]` — list of dicts with keys: `name`, `institution`, `year`, `status` (`"Em andamento"` | `"Concluído"`)
- `profile["targets"]` — list of strings shown as chips in the hero section
