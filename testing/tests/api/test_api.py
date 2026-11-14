"""API tests: real HTTP requests to the running app. They check the contract a client relies on:
status codes, content type and the shape of the JSON."""

import json
from urllib.error import HTTPError
from urllib.request import urlopen


def get(url):
    try:
        with urlopen(url, timeout=5) as response:
            return response.status, response.headers["Content-Type"], json.loads(response.read())
    except HTTPError as error:
        return error.code, error.headers["Content-Type"], json.loads(error.read())


def test_health(base_url):
    assert get(f"{base_url}/api/health") == (200, "application/json", {"status": "ok"})


def test_split_returns_money_as_strings(base_url):
    status, content_type, body = get(f"{base_url}/api/split?total=60&people=3&tip=10")
    assert status == 200
    assert content_type == "application/json"
    assert body == {"tip": "6.00", "total": "66.00", "per_person": "22.00"}


def test_bad_input_is_a_400_with_a_reason(base_url):
    status, _, body = get(f"{base_url}/api/split?total=abc&people=2")
    assert status == 400
    assert body == {"error": "total and tip must be numbers"}


def test_missing_parameters_are_a_400(base_url):
    status, _, body = get(f"{base_url}/api/split")
    assert status == 400
    assert "error" in body


def test_unknown_path_is_a_404(base_url):
    status, _, body = get(f"{base_url}/nope")
    assert (status, body) == (404, {"error": "not found"})
