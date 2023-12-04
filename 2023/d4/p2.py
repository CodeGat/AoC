import re

games_to_go: list[int] = []

# below is of the form: {card number: result, ...}
result_of_game: dict[int, int] = {}

with open("./2023/d4/in.txt") as f:
    while len(games_to_go) != 0:

    for game in f:
        card_num, winning_nums, my_nums = re.split("[:|]", game.rstrip())
        card_id: int = int(card_num.split()[1])
        wins: dict[str, int] = {win: 0 for win in winning_nums.split()}

        for my_num in my_nums.split():
            if my_num in wins:
                wins[my_num] = 1