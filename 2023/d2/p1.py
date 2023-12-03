with open("./2023/d2/in.txt", "r") as f:
    max_colours: dict[str, int] = {"red": 12, "green": 13, "blue": 14}
    result: int = 0

    for game in f:
        id_substring, game_substring = game.split(":")
        game_id: int = int(id_substring.split(" ")[1])

        # total_colours: dict[str, int] = {"red": 0, "green": 0, "blue": 0}

        game_is_possible: bool = True

        for subset in game_substring.strip().split(";"):
            for cubes in subset.strip().split(","):
                number_str, colour = cubes.strip().split(" ")
                if int(number_str) > max_colours[colour]:
                    game_is_possible = False
                # total_colours[colour] += int(number_str)

        # for colour in max_colours.keys():
        #     if total_colours[colour] > max_colours[colour]:
        #         game_is_possible = False
        #         print(f"I: Game {game_id} is impossible because {colour} {total_colours[colour]} > {max_colours[colour]}")

        if game_is_possible:
            print(f"P: Game {game_id} is possible")
            result += game_id

    print(result)
