# gunicorn.conf.py
loglevel = "debug"
bind = "0.0.0.0:8000"
workers = 2
worker_class = "uvicorn.workers.UvicornWorker"
wsgi_app= "app.main:app"