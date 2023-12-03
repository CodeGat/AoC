import functools

with open("./2023/d2/in.txt", "r") as f:
    max_colours: dict[str, int] = {"red": 0, "green": 0, "blue": 0}
    result: int = 0

    for game in f:
        id_substring, game_substring = game.split(":")
        game_id: int = int(id_substring.split(" ")[1])

        for subset in game_substring.strip().split(";"):
            for cubes in subset.strip().split(","):
                number_str, colour = cubes.strip().split(" ")
                number: int = int(number_str)

                if int(number_str) > max_colours[colour]:
                    max_colours[colour] = number

        result += functools.reduce(lambda a, b: a * b, max_colours.values())
        max_colours = dict.fromkeys(max_colours, 0)

    print(result)
