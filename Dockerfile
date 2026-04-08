# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install gradio pandas

EXPOSE 7860

CMD ["python", "inference.py"]