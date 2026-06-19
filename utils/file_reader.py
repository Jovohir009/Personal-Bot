from pathlib import Path

BASE_DIR = Path("data")


def read_file(file_path: str):
    return (BASE_DIR / file_path).read_text(encoding="utf-8")
