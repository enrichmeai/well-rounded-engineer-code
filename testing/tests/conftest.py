"""Shared pytest fixtures: a live copy of the app on a free port."""

import threading

import pytest

from tipsplit.server import make_server


@pytest.fixture(scope="session")
def base_url():
    server = make_server(port=0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    host, port = server.server_address[:2]
    yield f"http://{host}:{port}"
    server.shutdown()
    server.server_close()
