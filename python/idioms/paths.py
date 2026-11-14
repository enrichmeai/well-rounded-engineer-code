"""pathlib (Python 3.4): file paths as objects, not strings.

``/`` joins paths, and methods such as ``read_text``, ``glob`` and ``suffix`` replace a handful of
functions from ``os`` and ``os.path``. It works the same on Windows, macOS and Linux.
"""

from pathlib import Path


def write_notes(folder: Path, notes: dict[str, str]) -> list[Path]:
    folder.mkdir(parents=True, exist_ok=True)
    written = []
    for name, text in notes.items():
        path = folder / f"{name}.txt"
        path.write_text(text, encoding="utf-8")
        written.append(path)
    return written


def word_count_by_file(folder: Path) -> dict[str, int]:
    return {path.stem: len(path.read_text(encoding="utf-8").split()) for path in sorted(folder.glob("*.txt"))}
