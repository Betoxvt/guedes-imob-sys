# Dockerfile-API

# Base image
FROM python:3.13

# Add Astral UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Ensure PATH is set correctly
ENV PATH="/root/.local/bin/:$PATH"

# Define app port
EXPOSE 8000

# Copy the current directory contents into the container at /app
COPY . /app

# Define the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN uv pip install -r requirements.txt --system

# Comando para executar a aplicação
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]