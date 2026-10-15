# Data Information

This document provides information about the election data used in the project, including the structure of the CSV file and the data types of each column.

## CSV File Structure

The CSV file, named `eleicoes.csv`, contains the following columns:

| Column Name | Description | Data Type | Example |
|-------------|-------------|-----------|---------|
| ano         | Year of the election | int64 | 2024 |
| estado      | State where the election took place | category | SP |
| cidade      | City where the election took place | category | São Paulo |
| zona        | Electoral zone | category | 1 |
| secao       | Electoral section | category | 1 |
| cargo       | Position being contested | category | Mayor |
| candidato   | Candidate name | category | John Doe |
| partido     | Political party | category | ABC |
| numero      | Candidate number | category | 12345 |
| votos       | Number of votes received | int64 | 1000 |

## Notes

- The `category` data type is used for columns with a limited set of possible values to optimize memory usage.
- The `int64` data type is used for numerical columns to ensure accurate calculations and sufficient range.
