# Criar um script para gerar um arquivo CSV com os seguintes dados: nome, idade e cidade.
import csv
from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).parent.joinpath("data")
POPULATION_FILE_PATH = DATA_PATH.joinpath("estimativa_dou_2026.xlsx")
BRAZIL_POPULATION_CSV_PATH = DATA_PATH.joinpath("brazilian_population.csv")

df = pd.read_excel(POPULATION_FILE_PATH, sheet_name=1, header=1, skipfooter=2)
print(df)
pd.DataFrame.to_csv(df, BRAZIL_POPULATION_CSV_PATH, index=False)

def main(limit_rows: int):
    with open(BRAZIL_POPULATION_CSV_PATH, "r") as file:
        reader = csv.DictReader(file)
        for idx, row in enumerate(reader):
            if idx >= limit_rows:
                break
            print(row)

if __name__ == "__main__":
    main(limit_rows=20)