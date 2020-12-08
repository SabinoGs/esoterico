FROM python:3.9.1

WORKDIR /app

COPY . /app
RUN apt update && python3 -m pip install -e .

CMD ["gunicorn", "-c", "gunicorn_config.py", "--reload", "main:app"]