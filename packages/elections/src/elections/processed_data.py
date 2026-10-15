"""Processed data module for extracting election data from CSV files."""

import pandas as pd

from packages.elections.src import config


def extraction(file_path: str) -> pd.DataFrame:
    """Extraction data from CSV file.

    Args:
        file_path (str): Path to the CSV file containing the election data.

    Returns:
        pd.DataFrame: DataFrame containing the election data with appropriate data types.
    """

    # Define the columns and their respective names and data types for the CSV file.
    columns: dict[str, tuple[str, str]] = {
        "ano": ("ano", "int64"),
        "estado": ("estado", "category"),
        "cidade": ("cidade", "category"),
        "zona": ("zona", "category"),
        "secao": ("secao", "category"),
        "cargo": ("cargo", "category"),
        "candidato": ("candidato", "category"),
        "partido": ("partido", "category"),
        "numero": ("numero", "category"),
        "votos": ("votos", "int64"),
    }
    columns_dtype: dict[str, str] = {col: dtype for col, dtype in columns.values()}

    dataframe: pd.DataFrame = pd.read_csv(file_path, dtype=columns_dtype)
    return dataframe


def save_to_csv(data: pd.DataFrame, file_path: str) -> None:
    """Save the election data to a CSV file.

    Args:
        data (pd.DataFrame): The election data to save.
        file_path (str): The path to the CSV file.
    """
    data.to_csv(file_path, index=False)


def run():
    """Run the data extraction process and return the election data as a DataFrame."""
    dataframe = extraction(config.get_file_path("eleicoes.csv"))
    return dataframe


if __name__ == "__main__":
    print(run().head())

    print(f"Memory usage: {run().memory_usage(deep=True).sum()} bytes")
