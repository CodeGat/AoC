with open("./2023/d1/in.txt", "r") as file:
    total: int = 0

    for line in file:
        total += int(
            next(ch for ch in line if ch.isdigit())
            + next(ch for ch in reversed(line) if ch.isdigit())
        )

    print(total)
