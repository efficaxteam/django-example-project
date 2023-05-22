#!/bin/sh

# Wait for PostgreSQL to become available
until nc -z -v -w30 $POSTGRES_HOST 5432
do
  echo "Waiting for PostgreSQL to become available..."
  sleep 1
done

# Run migrations
echo "Running migrations..."
poetry run python core/manage.py migrate

# Start the application
exec "$@"