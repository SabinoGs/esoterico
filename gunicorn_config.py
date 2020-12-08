import os

bind = os.getenv('HOST', '0.0.0.0:5000')
loglevel = os.getenv("LOG_LEVEL", "DEBUG")
worker_class = os.getenv("WORKER_CLASS", 'uvicorn.workers.UvicornWorker')