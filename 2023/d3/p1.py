from string import punctuation
from re import Match, finditer, match
from typing import Iterator
from functools import reduce
import numpy as np

symbols: str = punctuation.replace('.', '')

def check_part_number(schematic: np.ndarray, y: int, x_start: int, x_end: int) -> bool:
    # keep in mind a potential negative x, y values when we are in the first row/column!
    surrounding_cells: np.ndarray = schematic[
        0 if y == 0 else y - 1 : y + 2, 0 if x_start == 0 else x_start - 1 : x_end + 1
    ]

    if match(f'[{symbols}]', str(surrounding_cells.flatten())):
        return True
    else:
        return False

with open("./2023/d3/in.txt") as f:
    # setup structures
    schematic: list[str] = [line.rstrip() for line in f]

    np_schematic: np.ndarray = np.array([list(line) for line in schematic])

    print(np_schematic)

    part_numbers: list[int] = []

    for y, line in enumerate(schematic):
        number_matches: Iterator[Match[str]] = finditer("[0-9]+", line)

        for number_match in number_matches:
            if check_part_number(np_schematic, y, number_match.start(), number_match.end()):
                part_numbers.append(int(number_match.group()))

    result: int = reduce(lambda x, y: x + y, part_numbers)

    print(result)
