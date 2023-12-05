from functools import reduce


def garden_map(seed_range: tuple[int, int], mapper: list[str]) -> list[tuple[int, int]]:
    mapped_seed_ranges: list[tuple[int, int]] = [seed_range]
    next_mapped_seed_ranges: list[tuple[int, int]] = []

    for map in mapper:
        for mapped_seed_range in mapped_seed_ranges:
            map_components: list[int] = [int(comp) for comp in map.split()]
            dest, src, range = map_components

            # how to we keep track of the dest ones?
            same_seed_ranges, mappable_seed_ranges = intersectional_split(
                mapped_seed_range[0], mapped_seed_range[1], src, src + range - 1
            )

            next_mapped_seed_ranges.extend(same_seed_ranges)

            # check p1 implementation of this function...just in case
            newly_mapped_seed_ranges: list[tuple[int, int]] = [
                (dest + start - src, dest + end - src)
                for start, end in mappable_seed_ranges
            ]
            next_mapped_seed_ranges.extend(newly_mapped_seed_ranges)

        mapped_seed_ranges = next_mapped_seed_ranges

    return mapped_seed_ranges


def intersectional_split(
    x1: int, x2: int, y1: int, y2: int
) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    # find which seed ranges are to be mapped and which ones arent
    # seed_range:   [           ]       |   [     ] |  [        ] |    [   ]
    # map_range:         [------------] | [----]    |    [----]   |  [-------]
    # final_ranges: [   ][------]       |   [--][ ] |  [][----][] |    [---]

    return ([], [])


with open("./2023/d5/in.txt") as f:
    seeds: list[int] = [int(seed) for seed in f.readline().split()[1:]]
    seed_range: list[tuple[int, int]] = [
        (start, start + range - 1) for start, range in zip(seeds[0::2], seeds[1::2])
    ]

    print(seed_range)

    f.readline()
    mappers: list[list[str]] = [map.split("\n")[1:] for map in f.read().split("\n\n")]

    for mapper in mappers:
        seed_range = list(map(lambda s: garden_map(s, mapper), seed_range))
        print(seed_range)

    print(min([start for start, _ in seed_range]))
