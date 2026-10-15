"""Use cases for processing election data."""

from typing import Literal

import pandas as pd

Position = Literal["Prefeito", "Vereador"]


def sample_data(
    data: pd.DataFrame, columns: list[str] | None = None, sample_size: int = 5
) -> pd.DataFrame:
    """Return a sample of the election data.

    Args:
        data (pd.DataFrame): The election data.
        columns (list[str] | None, optional): List of columns to include in the sample. Defaults to None.
        sample_size (int, optional): Number of sample rows to return. Defaults to 5.

    Returns:
        pd.DataFrame: Sample of the election data.
    """
    if columns is not None:
        data = data[columns]
    return data.sample(sample_size)


def calculate_votes_per_party(data: pd.DataFrame) -> pd.Series:
    """Calculate the total votes per party.

    Args:
        data (pd.DataFrame): The election data.

    Returns:
        pd.DataFrame: DataFrame containing the total votes per party.
    """
    votes_per_party: pd.Series = (
        data.groupby("partido")["votos"].sum().sort_values(ascending=False)
    )
    return votes_per_party


def calculate_winners(data: pd.DataFrame, position: Position) -> pd.DataFrame:
    """Return the winning candidate for the specified position in each city.

    Args:
        data (pd.DataFrame): Election data containing candidate votes.
        position (Position): The position to calculate winners for.

    Returns:
        pd.DataFrame: Winning candidate, party, vote total, and vote percentage
            for each city.
    """

    select_candidates: pd.DataFrame = data[data["cargo"] == position]

    votes_per_candidate: pd.DataFrame = (
        select_candidates.groupby(["estado", "cidade", "candidato", "partido"])["votos"]
        .sum()
        .reset_index()
    )

    total_votes_per_city: pd.Series = votes_per_candidate.groupby("cidade")[
        "votos"
    ].transform("sum")
    votes_per_candidate["pct"] = (
        votes_per_candidate["votos"] / total_votes_per_city * 100
    ).round(1)
    order_by_votes: pd.DataFrame = votes_per_candidate.sort_values(
        "votos", ascending=False
    )
    winner_per_city = order_by_votes.drop_duplicates("cidade")
    position_winners = winner_per_city.sort_values(
        "cidade", ascending=True
    ).reset_index(drop=True)
    return position_winners
