import re
from functools import reduce

with open('./2023/d4/in.txt') as f:
    result: int = 0

    for game in f:
        card_num, winning_nums, my_nums = re.split('[:|]', game.rstrip())
        wins: dict[str, int] = {win: 0 for win in winning_nums.split()}

        for my_num in my_nums.split():
            if my_num in wins:
                wins[my_num] = 1

        points: int = reduce(lambda a, b: a + b, wins.values())
        print(f"For {card_num} ({wins}) we got {points}")

        if points != 0:
            result += 2 ** (points - 1)

    print(result)
