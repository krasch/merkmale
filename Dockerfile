FROM python:3.14-slim-trixie
WORKDIR /app

RUN pip install --no-cache-dir pydantic-ai-slim[openai]

RUN useradd app
USER app

CMD ["python", "main.py"]