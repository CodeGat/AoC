from string import punctuation
from re import Match, finditer, match
from typing import Iterator
from functools import reduce

symbols: set[str] = set()

def check_addressable_cells_for_symbols(schematic: , cells: dict[str, int]) -> bool:
    """_summary_

    Args:
        cells (dict[str, int]): _description_

    Returns:
        bool: _description_
    """
    return match(punctuation.replace('.', ''), schematic)

def convert_to_addressable_cells(cells: dict[str, int]) -> dict[str[int]]:
    """_summary_

    Args:
        cells (dict[str, int]): _description_

    Returns:
        dict[str[int]]: _description_
    """
    

def check_part_number(schematic: list[str], y: int, x_start: int, x_end: int) -> int:
    """_summary_

    Args:
        schematic (list[str]): _description_
        y (int): _description_
        x_start (int): _description_
        x_end (int): _description_

    Returns:
        int: _description_
    """
    cells_surrounding_part_number: list[dict[str, int]] = [
        {'y': y - 1, 'x_start': x_start - 1, 'x_end': x_end + 1},
        {'y': y,     'x_start': x_start - 1, 'x_end': x_end + 1},
        {'y': y + 1, 'x_start': x_start - 1, 'x_end': x_end + 1}
    ]
    addressable_cells_surrounding_part_number: list[dict[str, int]]  = map(convert_to_addressable_cells, cells_surrounding_part_number)
    return reduce(lambda x, y: x and check_addressable_cells_for_symbols(y), addressable_cells_surrounding_part_number, True)

with open("./2023/d3/in.txt") as f:
    # setup structures
    schematic: list[str] = [line for line in f]
    part_numbers: list[int] = []

    for y, line in enumerate(schematic):
        number_matches: Iterator[Match[str]] = finditer('[0-9]+', line)

        for number_match in number_matches:
            part_numbers.append(check_part_number(schematic, y, number_match.start(), number_match.end()))

    result: int = reduce(lambda x, y: x + y, part_numbers)
        
    print(result)
