"""A tiny web app on Python's standard library: one page and a JSON API.

Run it:  python -m tipsplit.server --port 8000   then open http://127.0.0.1:8000/
"""

import argparse
import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from tipsplit.logic import split_bill

INDEX = Path(__file__).parent / "static" / "index.html"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 (the name is fixed by http.server)
        url = urlparse(self.path)
        if url.path == "/":
            self._send(HTTPStatus.OK, INDEX.read_bytes(), "text/html; charset=utf-8")
        elif url.path == "/api/health":
            self._json(HTTPStatus.OK, {"status": "ok"})
        elif url.path == "/api/split":
            query = {key: values[0] for key, values in parse_qs(url.query).items()}
            try:
                split = split_bill(query.get("total", ""), query.get("people", ""), query.get("tip", "0"))
            except ValueError as error:
                self._json(HTTPStatus.BAD_REQUEST, {"error": str(error)})
            else:
                self._json(HTTPStatus.OK, split.as_json())
        else:
            self._json(HTTPStatus.NOT_FOUND, {"error": "not found"})

    def _json(self, status: HTTPStatus, body: dict) -> None:
        self._send(status, json.dumps(body).encode("utf-8"), "application/json")

    def _send(self, status: HTTPStatus, body: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args) -> None:  # keep test output quiet
        pass


def make_server(port: int = 0) -> ThreadingHTTPServer:
    """Port 0 asks the operating system for any free port; read it back from ``server_address``."""
    return ThreadingHTTPServer(("127.0.0.1", port), Handler)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the tip-splitter app.")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    server = make_server(args.port)
    print(f"Serving on http://127.0.0.1:{server.server_address[1]}/  (Ctrl+C to stop)", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
