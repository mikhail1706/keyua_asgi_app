#!/usr/bin/env bash
echo "Start daphne server"
daphne -b 0.0.0.0 -p 8001 keyua_asgi_app.asgi:application
exec "$@"