from numpy import diff


with open("2024/d1/in.txt") as f:
    l1: list[int] = []
    l2: list[int] = []

    for line in f:
        e1, e2 = line.split("  ")
        l1.append(int(e1))
        l2.append(int(e2))

    l1.sort()
    l2.sort()

    print(sum([abs(e1 - e2) for e1, e2 in zip(l1, l2)]))