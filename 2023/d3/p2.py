from re import Match, finditer
from typing import Iterator
from functools import reduce
import numpy as np


def find_surrounding_gear(
    schematic: np.ndarray, y: int, x_start: int, x_end: int
) -> tuple[int, int] | None:
    # keep in mind a potential negative x, y values when we are in the first row/column!
    start_y_section = 0 if y == 0 else y - 1
    start_x_section = 0 if x_start == 0 else x_start - 1

    surrounding_cells: np.ndarray = schematic[
        start_y_section : y + 2, start_x_section : x_end + 1
    ]

    return next(
        (
            (start_x_section + x, start_y_section + y)
            for y, row in enumerate(surrounding_cells)
            for x, item in enumerate(row)
            if item == "*"
        ),
        None,
    )


with open("./2023/d3/in.txt") as f:
    # setup structures
    schematic: list[str] = [line.rstrip() for line in f]
    np_schematic: np.ndarray = np.array([list(line) for line in schematic])

    # dictionary of the form: "<x location of gear>,<y location of gear>": [<part number>, ...]
    # we only care about gears that have 2 part numbers, so we'll reduce on that later
    gears: dict[str, list[int]] = {}

    for y, line in enumerate(schematic):
        number_matches: Iterator[Match[str]] = finditer("[0-9]+", line)

        for number_match in number_matches:
            gear_coord = find_surrounding_gear(
                np_schematic, y, number_match.start(), number_match.end()
            )

            if gear_coord is not None:
                gear_x, gear_y = gear_coord
                gears.setdefault(f"{gear_x},{gear_y}", [])
                gears[f"{gear_x},{gear_y}"].append(int(number_match.group()))

    two_part_gears: list[list[int]] = [v for v in gears.values() if len(v) == 2]
    gear_ratios: list[int] = [
        reduce(lambda a, b: a * b, gear) for gear in two_part_gears
    ]
    result: int = reduce(lambda a, b: a + b, gear_ratios)

    print(result)
