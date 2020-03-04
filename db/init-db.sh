#!/bin/bash
set -e

USER="manejar"
DATABASE="manejar"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER "$USER";
    CREATE DATABASE "$DATABASE";
    GRANT ALL PRIVILEGES ON DATABASE "$USER" TO "$DATABASE";
EOSQL
