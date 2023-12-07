from functools import reduce
from uu import Error


def garden_map(seed_range: tuple[int, int], mapper: list[str]) -> list[tuple[int, int]]:
    mapped_seed_ranges: set[tuple[int, int]] = set()
    print(f">>> Mapping seed {seed_range}")

    for map in mapper:
        print(f"For map {map}...")
        map_components: list[int] = [int(comp) for comp in map.split()]
        dest, src, range = map_components

        same_seed_ranges, mappable_seed_ranges = intersectional_split(
            seed_range[0], seed_range[1], src, src + range - 1
        )

        mapped_seed_ranges.update(same_seed_ranges)

        newly_mapped_seed_ranges: list[tuple[int, int]] = [
            (dest + start - src, dest + end - src)
            for start, end in mappable_seed_ranges
        ]
        mapped_seed_ranges.update(newly_mapped_seed_ranges)
        print(
            f'kept: {same_seed_ranges}, newly mapped: {[f"{before[0]}-{before[1]} -> {after[0]}-{after[1]}" for before, after in zip(mappable_seed_ranges, newly_mapped_seed_ranges)]}\n'
        )

    return list(mapped_seed_ranges)

    # for map in mapper:
    #     print(f"For map {map} with seed_ranges {mapped_seed_ranges}...")
    #     for mapped_seed_range in mapped_seed_ranges:
    #         map_components: list[int] = [int(comp) for comp in map.split()]
    #         dest, src, range = map_components

    #         # how to we keep track of the dest ones?
    #         same_seed_ranges, mappable_seed_ranges = intersectional_split(
    #             mapped_seed_range[0], mapped_seed_range[1], src, src + range - 1
    #         )

    #         next_mapped_seed_ranges.extend(same_seed_ranges)

    #         # check p1 implementation of this function...just in case
    #         newly_mapped_seed_ranges: list[tuple[int, int]] = [
    #             (dest + start - src, dest + end - src)
    #             for start, end in mappable_seed_ranges
    #         ]
    #         next_mapped_seed_ranges.extend(newly_mapped_seed_ranges)
    #         print(f'kept: {same_seed_ranges}, newly mapped: {[f"{before[0]}-{before[1]} -> {after[0]}-{after[1]}" for before, after in zip(mappable_seed_ranges, newly_mapped_seed_ranges)]}\n')

    #     mapped_seed_ranges = next_mapped_seed_ranges
    #     next_mapped_seed_ranges = []

    # return mapped_seed_ranges


def intersectional_split(
    seed_range_start: int, seed_range_end: int, map_start: int, map_end: int
) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    # find which seed ranges are to be mapped and which ones aren't
    seed_ranges_that_stay_same: list[tuple[int, int]] = []
    seed_ranges_to_map: list[tuple[int, int]] = []

    print(
        f"intersection: checking intersection of seed range {seed_range_start}-{seed_range_end} and map {map_start}-{map_end}...",
        end="",
    )

    overlap_start, overlap_end = (
        max(seed_range_start, map_start),
        min(seed_range_end, map_end),
    )

    if overlap_start > overlap_end:
        # no overlap
        # seed: [    ]
        # map:         [--]
        # final:[    ]
        print("no overlap")
        seed_ranges_that_stay_same.append((seed_range_start, seed_range_end))

    elif overlap_start == map_start and overlap_end == map_end:
        # seed_range envelops all of map
        # seed: [           ]
        # map:     [----]
        # final:[ ][----][  ]
        print("seed range envelops map entirely")
        if seed_range_start != overlap_start:
            seed_ranges_that_stay_same.append((seed_range_start, overlap_start - 1))
        seed_ranges_to_map.append((overlap_start, overlap_end))
        if seed_range_end != overlap_end:
            seed_ranges_that_stay_same.append((overlap_end + 1, seed_range_end))

    elif overlap_start == seed_range_start and overlap_end == seed_range_end:
        # seed_range is enveloped by all of map
        # seed:   [   ]
        # map:  [--------]
        # final:  [---]
        print("seed range is enveloped by map entirely")
        seed_ranges_to_map.append((seed_range_start, seed_range_end))

    elif overlap_start == map_start:
        # seed_range overlaps from the left
        # seed:  [     ]
        # map:      [-----]
        # final: [ ][--]
        print("seed range overlaps from left of map")
        if seed_range_start != overlap_start:
            seed_ranges_that_stay_same.append((seed_range_start, overlap_start - 1))
        seed_ranges_to_map.append((overlap_start, seed_range_end))

    elif overlap_start == seed_range_start:
        # seed_range overlaps from the right
        # seed:     [    ]
        # map:   [----]
        # final:    [-][ ]
        print("seed range overlaps from right of map")
        seed_ranges_to_map.append((overlap_start, map_end))
        if seed_range_end != overlap_end:
            seed_ranges_that_stay_same.append((map_end + 1, seed_range_end))
    else:
        print(
            f"Somehow, {seed_range_start}-{seed_range_end} has no relation to {map_start}-{map_end}"
        )
        raise Error

    return seed_ranges_that_stay_same, seed_ranges_to_map


with open("./2023/d5/in.txt") as f:
    seeds: list[int] = [int(seed) for seed in f.readline().split()[1:]]
    seed_range: list[tuple[int, int]] = [
        (start, start + range - 1) for start, range in zip(seeds[0::2], seeds[1::2])
    ]

    print(seed_range)

    f.readline()
    mappers: list[list[str]] = [map.split("\n")[1:] for map in f.read().split("\n\n")]

    for mapper in mappers:
        print(f"Going to map {seed_range} with {mapper}...")
        mapped_seed_ranges: list[list[tuple[int, int]]] = list(
            map(lambda s: garden_map(s, mapper), seed_range)
        )
        seed_range = reduce(lambda l1, l2: l1 + l2, mapped_seed_ranges)
        print(seed_range)
        print("-" * 25)

    print(min([start for start, _ in seed_range]))
