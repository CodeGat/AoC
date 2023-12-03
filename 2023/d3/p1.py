import string
from functools import reduce

Loc = tuple[int, int]

def find_part_numbers(schematic: list[list[str]], x: int, y: int) -> list[int]:
    """_summary_

    Args:
        schematic (list[list[str]]): _description_
        x (int): _description_
        y (int): _description_

    Returns:
        list[int]: _description_
    """
    part_numbers: list[int] = []
    all_locations: list[Loc] = [
        (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), 
        (x,     y - 1),             (x,     y + 1),
        (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
    ]
    
    while (len(all_locations) != 0):
        locations_to_pop, part_number = get_part_number_from_location(all_locations)
        part_numbers.append(part_number)
        for location_to_pop in locations_to_pop:
            all_locations.remove(location_to_pop)
    
    return part_numbers

def get_part_number_from_location(locs: list[Loc]) -> tuple[list[Loc], int]:
    """_summary_

    Args:
        locs (list[Loc]): _description_

    Returns:
        tuple[list[Loc], int]: _description_
    """
    
    
with open("./2023/d3/in.txt") as f:
    # setup structures
    schematic: list[list[str]] = [[char for char in line.split(sep=None)] for line in f]
    symbols: set[str] = set(string.punctuation.replace('.', ''))
    symbol_locations: list[tuple[int, int]] = [(x, y) for y, line in enumerate(schematic) for x, item in enumerate(line) if item in symbols]
    
    part_numbers: list[list[int]] = map(lambda loc: find_part_numbers(schematic, loc[0], loc[1]), symbol_locations)
    result: int = reduce(lambda x, y: x + y, part_numbers)
    
    print(result)
    