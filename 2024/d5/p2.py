from math import ceil


with open("./2024/d5/in.txt") as f:
    # of the form {number, ({numbers before, numbers after})}
    rules: dict[int, tuple[list[int], list[int]]] = {}
    badly_ordered_updates: list[list[int]] = []
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
        update_bad: bool = False

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
                badly_ordered_updates.append(update)
                break

        print("\n")

    for badly_ordered_update in badly_ordered_updates:
        while i != len(badly_ordered_update):
            required_before = rules[badly_ordered_update[i]][0]
            required_after = rules[badly_ordered_update[i]][1]
            currently_before = badly_ordered_update[:i]
            currently_after = badly_ordered_update[i+1:]

            if currently_before != [] and set(currently_before).issubset(required_after):
                print(f"Page {update[i]} does not follow the rules, moving currently before to required after...")
                changes_required = set(currently_before).intersection(required_after)
                print(changes_required)
                for change in changes_required:
                    badly_ordered_update.insert(i, change)
            elif currently_after != [] and set(currently_after).issubset(required_before):
                print(f"Page {update[i]} does not follow the rules, moving currently after to required before...")
                changes_required = set(currently_after).intersection(required_before)
                print(changes_required)
                for change in changes_required:
                    badly_ordered_update.insert(i+1, change)

            print(badly_ordered_update)

            i += 1








    print(f"RESULT: {result}")
