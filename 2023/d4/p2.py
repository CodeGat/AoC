import re
from functools import reduce

def 

with open("./2023/d4/in.txt") as f:
    games: list[str] = [game.rstrip() for game in f]
    games_to_go: dict[int, int] = []

    # below is of the form: {card: {card1: games, card2: games, ...}, ...}
    game_results: dict[int, int] = {}
    game_ix: int = 1

    while games_to_go != 0:
        card_num, winning_nums, my_nums = re.split("[:|]", games[games_to_go.pop()])
        card_id: int = int(card_num.split()[1])

        if card_id in game_results.keys():
            games_to_go = distribute_points_downward(games_to_go, game_results[card_id])
            continue

        wins: dict[int, int] = {int(win): 0 for win in winning_nums.split()}

        for my_num in my_nums.split():
            if my_num in wins:
                wins[int(my_num)] = 1
        
        points: int = reduce(lambda a, b: a + b, wins.values())
                
        
