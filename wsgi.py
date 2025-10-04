# wsgi.py — puente robusto
try:
    # Caso 1: app.py define "app = Flask(__name__)"
    from app import app as application
except ImportError:
    # Caso 2: app.py define "application = Flask(__name__)" u otro nombre
    from app import application
# Gunicorn buscará "app"
app = application

