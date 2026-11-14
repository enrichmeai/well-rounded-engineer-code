"""Context managers: the ``with`` statement (PEP 343, Python 2.5).

``with`` guarantees that clean-up runs, even when the block raises. You can write one as a class
with ``__enter__`` and ``__exit__``, or as a generator with ``contextlib.contextmanager``.
"""

import time
from contextlib import contextmanager
from collections.abc import Iterator


class Timer:
    """Measures how long the ``with`` block took. A class-based context manager."""

    def __init__(self, clock=time.perf_counter):
        self._clock = clock
        self.elapsed: float | None = None

    def __enter__(self) -> "Timer":
        self._start = self._clock()
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        self.elapsed = self._clock() - self._start
        return False  # do not swallow exceptions


@contextmanager
def temporary_setting(settings: dict, key: str, value) -> Iterator[dict]:
    """Changes one setting for the length of the block, then puts the old value back."""
    missing = object()
    old = settings.get(key, missing)
    settings[key] = value
    try:
        yield settings
    finally:
        if old is missing:
            del settings[key]
        else:
            settings[key] = old
