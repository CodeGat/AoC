import operator

with open("./2024/d2/in.txt") as f:
    safe_reports: int = 0

    for puzzle in f:
        levels: list[int] = [int(l) for l in puzzle.split()]

        # Check whether the operator will be >, <...or if they're equal (bad!)
        if levels[0] == levels[1]:
            # If they're equal, they're not increasing or decreasing, so we skip
            print(f"Skipping {puzzle} because we can't determine increase/decrease from first comparison")
            continue

        comparison_func = operator.lt if levels[0] < levels[1] else operator.gt
        e1 = 0
        e2 = 1
        levels_in_safe_range: bool = True

        while e2 < len(levels):
            # if the two levels are >/< (depending on the first comparison) and the difference is between 1-3
            if not comparison_func(levels[e1], levels[e2]) or not 0 < abs(levels[e1] - levels[e2]) < 4:
                print(f"Unsafe: {levels} - Comparing {levels[e1]} and {levels[e2]} failed, continuing...")
                levels_in_safe_range = False
                e1 += 1
                e2 += 1
                continue

            e1 += 1
            e2 += 1

        if levels_in_safe_range:
            print(f"Safe: {levels}")
            safe_reports += 1

    print(f"Safe reports: {safe_reports}")

