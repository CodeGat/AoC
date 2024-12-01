with open("2024/d1/in.txt") as f:
    # Our two lists
    l1: list[int] = []
    l2: list[int] = []
    # How many times has an element in l1 been seen in l2?
    occurrences: dict[int, int] = {}
    # Has an element in l1 already been computed? We don't want to compute it again...
    already_seen: dict[int, bool] = {}
    # This is the output -  the similarity score!
    similarity_score: int = 0

    for line in f:
        e1, e2 = line.split("  ")
        l1.append(int(e1))
        l2.append(int(e2))

    for e1 in l1:
        for e2 in l2:
            if e1 in already_seen:
                # We've already gone through l2 for this e1, skip it!
                break

            if e1 == e2:  # we increment the number of e1s seen in l2
                occurrences[e1] = occurrences.setdefault(e1, 0) + 1


        print(f"Similarity score for {e1} = {occurrences.get(e1, 0)}")
        similarity_score += e1 * occurrences.get(e1, 0)
        already_seen[e1] = True

    print(f"Similarity score: {similarity_score}!")