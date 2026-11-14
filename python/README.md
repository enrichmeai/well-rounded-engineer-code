# Python idioms

Seven small modules, each showing one idiom that makes Python code shorter and clearer, and each with pytest
tests that pin down exactly what it does.

Read first: [the Python section of the guide](https://enrichmeai.com/well-rounded-engineer/python/).

## What you need

Python 3.10 or newer (`python3 --version`). 3.10 is the minimum because `match` and `X | None` arrived in 3.10.

## Run it

```bash
cd python
python3 -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

You should see `27 passed`.

## The idioms

| Idiom | Since | Module | Tests |
|---|---|---|---|
| The `with` statement and context managers | 2.5 (PEP 343) | [`idioms/context_managers.py`](idioms/context_managers.py) | [`tests/test_context_managers.py`](tests/test_context_managers.py) |
| Generators, `yield` and `yield from` | 2.2 (PEP 255), 3.3 (PEP 380) | [`idioms/generators.py`](idioms/generators.py) | [`tests/test_generators.py`](tests/test_generators.py) |
| `pathlib` | 3.4 | [`idioms/paths.py`](idioms/paths.py) | [`tests/test_paths.py`](tests/test_paths.py) |
| Type hints, `list[int]`, `X \| None` | 3.5 (PEP 484), 3.9 (PEP 585), 3.10 (PEP 604) | [`idioms/typing_basics.py`](idioms/typing_basics.py) | [`tests/test_typing_basics.py`](tests/test_typing_basics.py) |
| f-strings, and `{name=}` for debugging | 3.6 (PEP 498), 3.8 | [`idioms/fstrings.py`](idioms/fstrings.py) | [`tests/test_fstrings.py`](tests/test_fstrings.py) |
| Dataclasses (`slots=True` since 3.10) | 3.7 (PEP 557) | [`idioms/data_classes.py`](idioms/data_classes.py) | [`tests/test_data_classes.py`](tests/test_data_classes.py) |
| Structural pattern matching, `match` | 3.10 (PEP 634) | [`idioms/matching.py`](idioms/matching.py) | [`tests/test_matching.py`](tests/test_matching.py) |

The "Since" column was checked against the "What's New" pages in CPython's own source,
[`Doc/whatsnew/`](https://github.com/python/cpython/tree/main/Doc/whatsnew): `2.2.rst` (PEP 255), `2.5.rst`
(PEP 343, `contextlib.contextmanager`), `3.3.rst` (PEP 380), `3.4.rst` (`pathlib`), `3.5.rst` (PEP 484),
`3.6.rst` (PEP 498), `3.7.rst` (PEP 557), `3.8.rst` (f-strings support `=`), `3.9.rst` (PEP 585) and `3.10.rst`
(PEP 634, PEP 604, the `slots` parameter of `@dataclass`).

## Try this

1. In `idioms/data_classes.py`, change `field(default_factory=list)` to `= []`. What does Python say, and why is
   that a kindness?
2. Add a `case ["drop", item]:` branch to `handle_command` in `idioms/matching.py`, and a test for it first. Watch
   the test fail, then make it pass.
3. Write `read_lines(path)` as a generator that yields one line of a file at a time, and test it with pytest's
   `tmp_path` fixture (see `tests/test_paths.py`).
4. Install `mypy` (`pip install mypy`), run `mypy idioms`, then call `average("not a list")` somewhere and run it
   again. The tests never ran that line; the type checker still found it.

## Read next

- [Python, in the guide](https://enrichmeai.com/well-rounded-engineer/python/)
- [`../testing/`](../testing/) shows the same pytest used for unit, API and browser tests.
