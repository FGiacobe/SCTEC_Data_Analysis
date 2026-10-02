# Criar um script para gerar um arquivo CSV com os seguintes dados: nome, idade e cidade.
import csv
from pathlib import Path

import pandas as pd

DATA_PATH: Path = Path(__file__).parent.joinpath("data")
EXCEL_FILE_PATH: Path = DATA_PATH.joinpath("estimativa_dou_2026.xlsx")
SAVE_CSV_PATH: Path = DATA_PATH.joinpath("brazilian_population.csv")


def transform_excel_to_csv() -> None:
    """Converte uma planilha Excel em arquivo CSV."""
    excel_data: pd.DataFrame = pd.read_excel(EXCEL_FILE_PATH, sheet_name=1, header=1, skipfooter=2)
    pd.DataFrame.to_csv(excel_data, SAVE_CSV_PATH, index=False)


def main(limit_rows: int):
    """Exibe as primeiras linhas do CSV gerado até o limite informado."""
    with open(SAVE_CSV_PATH, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for idx, row in enumerate(reader):
            if idx >= limit_rows:
                break
            print(row)

if __name__ == "__main__":
    main(limit_rows=20)
