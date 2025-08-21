#!/bin/sh
# /api/wait-for-db.sh
# wait-for-db.sh

set -e

host="$1"
shift
cmd="$@"

# Extrai a senha, usuário, nome do banco e porta da URL do banco
# postgresql://admin:password123@db:5432/agendadb
user=$(echo $DATABASE_URL | awk -F'://' '{print $2}' | awk -F':' '{print $1}')
password=$(echo $DATABASE_URL | awk -F':' '{print $3}' | awk -F'@' '{print $1}')
dbname=$(echo $DATABASE_URL | awk -F'/' '{print $4}')
export PGPASSWORD=$password

until psql -h "$host" -U "$user" -d "$dbname" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd