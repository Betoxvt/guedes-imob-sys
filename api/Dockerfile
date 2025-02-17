# Dockerfile-API

FROM python:3.13

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# ENV PATH="/root/.local/bin/:$PATH"

RUN apt-get update && apt-get install -y locales \
    && sed -i '/pt_BR.UTF-8/s/^# //g' /etc/locale.gen \
    && locale-gen pt_BR.UTF-8

ENV LANG=pt_BR.UTF-8
ENV LANGUAGE=pt_BR:pt
ENV LC_ALL=pt_BR.UTF-8

EXPOSE 8000

COPY . /app

WORKDIR /app

# RUN uv pip install -r requirements.txt --system

RUN uv add -r requirements.txt -U

CMD ["uv", "run", "uvicorn", "main:app", "--host", "estate_system-api-1", "--port", "8000"]
