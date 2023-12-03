from string import punctuation
from re import Match, finditer
from typing import Iterator

with open("./2023/d3/in.txt") as f:
    # setup structures
    schematic: list[str] = [line for line in f]
    symbols: set[str] = set(punctuation.replace('.', ''))
    number_locations: list[dict[str, int]] = []

    for y, line in enumerate(schematic):
        number_matches: Iterator[Match[str]] = finditer('[0-9]+', line)

        for number_match in number_matches:
            number_locations.append({'y': y, 'x_start': number_match.start(), 'x_end': number_match.end()})

    for number_location in number_locations:
