FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["granian", "app.__main__:app", "--host", "0.0.0.0", "--port", "5000"]
