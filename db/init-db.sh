DB_PASSWORD=$(cat /run/secrets/db_password)

psql -v "ON_ERROR_STOP=1" -U postgres -c "CREATE USER betoxvt WITH PASSWORD '$DB_PASSWORD';"
psql -v "ON_ERROR_STOP=1" -U postgres -c "CREATE DATABASE estate_system_db OWNER betoxvt;"
psql -v "ON_ERROR_STOP=1" -U postgres -d estate_system_db -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO betoxvt;"
psql -v "ON_ERROR_STOP=1" -U postgres -d estate_system_db -c "GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO betoxvt;"