"""Utility functions for formatting numbers according to Brazilian conventions."""


def br_number(number: float | str, decimals: int = 2) -> str:
    """Format a number according to Brazilian conventions.

    Args:
        number (float | str): The number to be formatted.
        decimals (int): The number of decimal places to format the number with. Default is 2.

    Returns:
        str: The formatted number as a string with thousands separator. Example: 1.234.567,89
    """
    # Deve coverter formatos como "1234567,59" para "1.234.567,59" ou "1234567.59" para "1.234.567,59"
    if isinstance(number, str):
        number = number.replace(",", ".")
        number = float(number)
    formatted_number = (
        f"{number:,.{decimals}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )
    return str(formatted_number)


if __name__ == "__main__":
    N_SAMPLE_01 = "123456"
    N_SAMPLE_02 = "123456,56"
    N_SAMPLE_03 = "123456.56"

    formatted_number_01 = br_number(N_SAMPLE_01, 0)
    formatted_number_02 = br_number(N_SAMPLE_02, 2)
    formatted_number_03 = br_number(N_SAMPLE_03, 2)

    print(formatted_number_01)
    print(formatted_number_02)
    print(formatted_number_03)
