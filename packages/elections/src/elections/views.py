"""Views for displaying election data using rich."""

import pandas as pd
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from packages.elections.src.elections import processed_data, use_cases
from packages.elections.src.utils import br_number


def resume_view(data: pd.DataFrame) -> None:
    """Display a summary of the election dataset.

    Args:
        data (pd.DataFrame): The election data to summarize.
    """

    total_registers: int = len(data)
    total_votes: int = int(data["votos"].sum())
    total_cities: int = data["cidade"].nunique()
    total_candidates: int = data["candidato"].nunique()

    title = "[bold]Eleições 2024 (dados fictícios)[/bold]"
    text = (
        f"[bold]Registros:[/] [bold cyan]{total_registers}[/bold cyan]\t\t"
        f"[bold]Votos:[/] [bold cyan]{total_votes}[/bold cyan]\t\t"
        f"[bold]Cidades:[/] [bold cyan]{total_cities}[/bold cyan]\t\t"
        f"[bold]Candidatos:[/] [bold cyan]{total_candidates}[/bold cyan]"
    )

    Console().print(
        Panel(text, title=title, expand=True, safe_box=True, width=120, padding=(1, 3))
    )


def sample_view(data: pd.DataFrame, sample_size: int = 5) -> None:
    """Display a sample of the election data.

    Args:
        data (pd.DataFrame): The election data.
        sample_size (int, optional): Number of sample rows to display. Defaults to 5.
    """
    columns = ["estado", "cidade", "secao", "cargo", "candidato", "partido", "votos"]
    title = f"Amostragem de Dados com {sample_size} Linhas"
    sample = use_cases.sample_data(data, columns=columns, sample_size=sample_size)

    table = Table(
        title=title, header_style="bold cyan", min_width=120, title_style="bold"
    )

    for column in columns:
        table.add_column(column.title())

    for _, row in sample.iterrows():
        table.add_row(*[str(row[col]) for col in columns])

    Console().print(table)


def votes_per_party_graphic_view(data: pd.DataFrame) -> None:
    """Display the total votes per party.

    Args:
        data (pd.DataFrame): The election data.
    """
    votes_per_party = use_cases.calculate_votes_per_party(data).reset_index()
    total_votes = votes_per_party["votos"].sum()
    title = "Votos por Partido"

    table = Table(
        title=title, header_style="bold cyan", min_width=120, title_style="bold"
    )
    table.add_column("Partido")
    table.add_column("Votos", justify="right")
    table.add_column("%", justify="right")
    table.add_column("Gráfico", justify="left")

    for _, row in votes_per_party.iterrows():
        percentage = (row["votos"] / total_votes) * 100
        graphic_type = "[cyan]░[/cyan]" * int(percentage / 1)
        table.add_row(
            row["partido"],
            br_number(row["votos"], 0),
            f"{percentage:.2f}%",
            graphic_type,
        )

    Console().print(table)


def winners_view(data: pd.DataFrame, position: use_cases.Position) -> None:
    """Display the winning candidates for the specified position in each city.

    Args:
        data (pd.DataFrame): The election data.
    """
    mayor_winners: pd.DataFrame = use_cases.calculate_winners(data, position)
    title: str = f"Vencedores das Eleições Municipais para {position}"

    table: Table = Table(
        title=title, header_style="bold cyan", min_width=120, title_style="bold"
    )
    table.add_column("UF")
    table.add_column("Cidade")
    table.add_column("Candidato")
    table.add_column("Partido")
    table.add_column("Votos", justify="right")
    table.add_column("%", justify="right")

    for _, row in mayor_winners.iterrows():
        table.add_row(
            row["estado"],
            row["cidade"],
            row["candidato"],
            row["partido"],
            br_number(row["votos"], 0),
            f"{row['pct']:.2f}%",
        )

    Console().print(table)


def run(data: pd.DataFrame):
    """Main function to extract election data and display various views.

    This function extracts the election data from the configured file path,
    then displays a summary view, a sample view, the votes per party graphic,
    and the winners for both the mayor and councilor positions.
    """
    resume_view(data)
    sample_view(data, sample_size=5)
    votes_per_party_graphic_view(data)
    winners_view(data, position="Prefeito")
    winners_view(data, position="Vereador")


if __name__ == "__main__":
    df = processed_data.run()
    run(df)
