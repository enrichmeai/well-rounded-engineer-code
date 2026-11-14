#!/usr/bin/env bash
# Starts the app, runs the Postman collection against it with Newman, then stops the app.
# Usage (from the testing/ folder):  scripts/run-newman.sh
# Set PORT to use another port, and PYTHON to use another interpreter.
set -euo pipefail
cd "$(dirname "$0")/.."

PORT="${PORT:-8765}"
PYTHON="${PYTHON:-python3}"
"$PYTHON" -m tipsplit.server --port "$PORT" &
SERVER_PID=$!
trap 'kill "$SERVER_PID" 2>/dev/null || true' EXIT

# Wait up to 10 seconds for OUR app to answer its health check.
ready=no
for _ in $(seq 1 50); do
  if ! kill -0 "$SERVER_PID" 2>/dev/null; then
    echo "The app did not start (is port $PORT already in use? try PORT=8766 $0)" >&2
    exit 1
  fi
  if "$PYTHON" -c "import json, urllib.request, sys; r = urllib.request.urlopen('http://127.0.0.1:$PORT/api/health', timeout=1); sys.exit(json.load(r) != {'status': 'ok'})" 2>/dev/null; then
    ready=yes
    break
  fi
  sleep 0.2
done
if [ "$ready" != yes ]; then
  echo "The app did not answer on port $PORT within 10 seconds" >&2
  exit 1
fi

npx newman run postman/tipsplit.postman_collection.json --env-var "baseUrl=http://127.0.0.1:$PORT"
