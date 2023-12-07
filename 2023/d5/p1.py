from functools import reduce


def garden_map(seed: int, mapper: list[str]) -> int:
    mapped_seed: int = seed

    for map in mapper:
        map_components: list[int] = [int(comp) for comp in map.split()]
        dest, src, range = map_components

        print(f"For seed {seed}, {src} < {seed} < {src + range - 1}: ", end="")

        if src <= seed <= src + range - 1:
            mapped_seed = dest + seed - src
            print(f"mapped to {mapped_seed}")
        else:
            print("")

    return mapped_seed


with open("./2023/d5/in.txt") as f:
    seeds: list[int] = [int(seed) for seed in f.readline().split()[1:]]
    f.readline()
    mappers: list[list[str]] = [map.split("\n")[1:] for map in f.read().split("\n\n")]

    print(seeds)

    # seeds: list[int] = [garden_map(s, m) for m in mappers for s in seeds]
    for mapper in mappers:
        seeds = list(map(lambda s: garden_map(s, mapper), seeds))
        print(seeds)

    print(min(seeds))
