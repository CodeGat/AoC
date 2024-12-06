from math import ceil


with open("./2024/d5/in.txt") as f:
    # of the form {number, ({numbers before, numbers after})}
    rules: dict[int, tuple[list[int], list[int]]] = {}
    result: int = 0

    while (line := f.readline()) != "\n":
        before, after = [int(l) for l in line.split("|")]
        if before in rules:
            rules[before][1].append(after)
        else:
            rules[before] = ([], [after])

        if after in rules:
            rules[after][0].append(before)
        else:
            rules[after] = ([before], [])

    for update_str in f.readlines():
        update: list[int] = [int(u) for u in update_str.split(",")]
        update_good: bool = True

        print(f"*** FOR UPDATE {update} ***")

        for i in range(len(update)):
            required_before = rules[update[i]][0]
            required_after = rules[update[i]][1]
            currently_before = update[:i]
            currently_after = update[i+1:]

            print(f"For {update[i]}:")
            print(f"Before: {currently_before}, requires: {required_before}")
            print(f"After: {currently_after}, requires: {required_after}")

            if (currently_before != [] and set(currently_before).issubset(required_after)) or (currently_after != [] and set(currently_after).issubset(required_before)):
                print(f"Page {update[i]} does not follow the rules!")
                update_good = False
                break

        print("\n")

        if update_good:
            print(f"Middle number of {len(update)} is {ceil(len(update)/2)} ({update[ceil(len(update)/2)-1]})")
            result += update[ceil(len(update)/2)-1]

    print(f"RESULT: {result}")
