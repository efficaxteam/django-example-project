FROM python:3.10-slim-buster

WORKDIR /app

LABEL authors="Efficax Team"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app:/app/project:$PYTHONPATH

RUN apt-get update && apt-get install -y netcat
RUN pip install poetry

COPY . /app

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --with linux

EXPOSE 8000

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]

