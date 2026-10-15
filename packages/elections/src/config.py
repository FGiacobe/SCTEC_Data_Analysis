"""Configuration settings for the elections data file."""

from pathlib import Path

BASE_PATH = Path.cwd()


def get_file_path(file: str) -> str:
    """Get the full file path for the election data CSV file."""
    return str(BASE_PATH.joinpath("data", file))
