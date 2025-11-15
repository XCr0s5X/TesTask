FROM python:3.12-slim

# system deps for some wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl gcc libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY ./litestar_service /app

RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# run as non-root
RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

# start uvicorn in factory mode (create_app)
CMD ["uvicorn", "app.__main__:create_app", "--factory", "--host", "0.0.0.0", "--port", "5000"]
