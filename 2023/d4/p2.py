import re
from functools import reduce


def distribute_later_games(
    current_card_played: int, games_to_go: list[int], amount_of_bonus_cards: int
) -> list[int]:
    if amount_of_bonus_cards == 0:
        return games_to_go

    print(
        f"Adding {games_to_go[current_card_played]} cards to the next {amount_of_bonus_cards} games played after Card {current_card_played + 1}"
    )
    print(games_to_go)

    for i in range(1, amount_of_bonus_cards + 1):
        games_to_go[current_card_played + i] += games_to_go[current_card_played]
    print("Leaving:")
    print(games_to_go)

    print("------------------------------")

    return games_to_go


with open("./2023/d4/in.txt") as f:
    games: list[str] = [game.rstrip() for game in f]
    cards: int = len(games)

    # below is of the form: games_to_go[i] = Card i+1's games left to play
    games_to_go: list[int] = [1] * cards

    # aka while we haven't exhausted all the previous card games, and the final game
    for card_ix in range(cards):
        _, winning_nums, my_nums = re.split("[:|]", games[card_ix])

        wins: dict[str, int] = {win: 0 for win in winning_nums.split()}

        for my_num in my_nums.split():
            if my_num in wins:
                wins[my_num] = 1

        bonus_cards: int = reduce(lambda a, b: a + b, wins.values())

        print(f"Card {card_ix + 1} won {bonus_cards} bonus cards!")
        games_to_go = distribute_later_games(card_ix, games_to_go, bonus_cards)

    print(reduce(lambda a, b: a + b, games_to_go))
