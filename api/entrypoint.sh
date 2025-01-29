DB_PASSWORD=$(cat /run/secrets/db_password)

export DATABASE_URL="postgres://betoxvt:${DB_PASSWORD}@db:5432/estate_system_db"

exec uv run uvicorn main:app --host 0.0.0.0 --port 8000