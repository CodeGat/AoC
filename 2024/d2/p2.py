import operator

def check_levels(levels: list[int]) -> bool:
    # Check whether the operator will be >, <...or if they're equal (bad!)
    if levels[0] == levels[1]:
        return False

    comparison_func = operator.lt if levels[0] < levels[1] else operator.gt
    e1 = 0
    e2 = 1

    while e2 < len(levels):
        # if the two levels are >/< (depending on the first comparison) and the difference is between 1-3
        if not comparison_func(levels[e1], levels[e2]) or not 0 < abs(levels[e1] - levels[e2]) < 4:
            print(f"Unsafe: {levels} - Comparing {levels[e1]} and {levels[e2]} failed.")
            return False

        e1 += 1
        e2 += 1

    return True


with open("./2024/d2/in.txt") as f:
    safe_reports: int = 0

    for puzzle in f:
        levels: list[int] = [int(l) for l in puzzle.split()]

        # Check the levels without removing an index first
        if check_levels(levels):
            safe_reports += 1
            continue

        print("------")

        # TODO: More efficient: You only need to start deleting indexes when there is a failure.
        for index_for_deletion in range(len(levels)):
            levels_with_deleted_index: list[int] = list(levels)
            del levels_with_deleted_index[index_for_deletion]

            print(f"Testing {index_for_deletion} variant of {levels}: {levels_with_deleted_index}")

            if check_levels(levels_with_deleted_index):
                safe_reports += 1
                break

    print(f"Safe reports: {safe_reports}")

