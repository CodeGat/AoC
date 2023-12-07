from functools import reduce
from typing import Optional


def gardening_map(seed_range: range, maps: list[str]) -> list[range]:
    mapped_seed_range: list[range] = []
    # maybe it should be a set?

    for map in maps:
        dest_str, src_str, rng_str = map.split()
        # TODO: check if ranges are correct!
        dest: range = range(int(dest_str), int(dest_str) + int(rng_str) - 1)
        src: range = range(int(src_str), int(src_str) + int(rng_str) - 1)

        same, mappable = split_intersection(seed_range, src)
        mapped: Optional[range] = None

        if mappable is not None:
            mapped_seed_range.remove(mappable)
            mapped = range(
                dest.start + (mappable.start - src.start),
                dest.start + (mappable.stop - src.start),
            )
            mapped_seed_range.append(
                mapped
            )

        mapped_seed_range.extend(same)

        print(
            f"For ({seed_range.start}-{seed_range.stop}) with map ({src.start}-{src.stop})->({dest.start}-{dest.stop}) | same {[f'({s.start}-{s.stop})' for s in same]}{f', mapped ({mappable.start}-{mappable.stop})->({mapped.start}-{mapped.stop})' if mappable is not None and mapped is not None else ''}"
        )
    print("-" * 10)

    return mapped_seed_range


def split_intersection(
    seed_range: range, map_range: range
) -> tuple[list[range], Optional[range]]:
    same: list[range] = []
    mappable: Optional[range] = None

    intersection: range = range(
        max(seed_range.start, map_range.start), min(seed_range.stop, map_range.stop)
    )

    # test out intersection.start == intersection.stop?

    if intersection.start > intersection.stop:  # there is no overlap
        # seed   [    ]
        # map           [----]
        # result [    ]
        same.append(seed_range)
    elif (
        intersection.start == seed_range.start and intersection.stop == seed_range.stop
    ):
        # seed    [    ]   | [   ]
        # map    [-------] | [---]
        # result  [----]   | [---]
        mappable = seed_range
    elif intersection.start == seed_range.start:
        # seed     [    ] | [    ]
        # map    [---]    | [-------]
        # result   [-][ ] | [----]
        mappable = range(seed_range.start, intersection.stop)
        if seed_range.stop > intersection.stop:
            same.append(range(intersection.stop + 1, seed_range.stop))
    elif intersection.stop == seed_range.stop:
        # seed   [    ]    |   [   ]
        # map      [-----] | [-----]
        # result [][--]    |   [---]
        if seed_range.start < intersection.start:
            same.append(range(seed_range.start, intersection.start - 1))
        mappable = range(intersection.start, intersection.stop)
    elif intersection.start > seed_range.start and intersection.stop < seed_range.stop:
        # seed   [          ]
        # map       [---]
        # result [ ][---][  ]
        same.append(range(seed_range.start, intersection.start - 1))
        mappable = range(intersection.start, intersection.stop)
        same.append(range(intersection.stop + 1, seed_range.stop))

    return same, mappable


with open("./2023/d5/in.txt") as f:
    seeds: list[int] = [int(seed) for seed in f.readline().split()[1:]]
    seed_ranges: list[range] = [
        range(start, start + rng - 1) for start, rng in zip(seeds[0::2], seeds[1::2])
    ]
    mapped_seed_ranges: list[range] = []

    print(seed_ranges)

    f.readline()
    mappers: list[list[str]] = [map.split("\n")[1:] for map in f.read().split("\n\n")]

    for seed_range in seed_ranges:
        print(f"Going to run ({seed_range.start}-{seed_range.stop}) through all the mappers...")
        partially_mapped_seed_range: list[range] = [seed_range]

        for mapper in mappers:
            print(f"Running {[f'({p.start}-{p.stop})' for p in partially_mapped_seed_range]} through {mapper}")
            partially_mapped_seed_ranges: list[list[range]] = list(
                map(lambda s: gardening_map(s, mapper), partially_mapped_seed_range)
            )
            partially_mapped_seed_range = reduce(
                lambda l1, l2: l1 + l2, partially_mapped_seed_ranges
            )

        mapped_seed_ranges.extend(partially_mapped_seed_range)

    print(min([m.start for m in mapped_seed_ranges]))
