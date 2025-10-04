# sfig-tasks (Flask)

App simple para controlar actividades (fechas, avance, estado).

## Local
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Render.com (Free)
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`
- Env: `SECRET_KEY` con un valor seguro
