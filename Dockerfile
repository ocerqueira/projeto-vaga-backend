FROM python:3.13-slim
WORKDIR /app


COPY pyproject.toml uv.lock ./


RUN pip install --upgrade pip uv


RUN pip install .   # roda pip install, que usa o PEP 517


COPY . .


EXPOSE 8000

ENV PYTHONPATH=/app



CMD ["bash", "-c", "python scripts/seed.py && uvicorn app.app:app --host 0.0.0.0 --port 8000"]

