import re

with open("./2023/d6/in.txt") as f:
    times_str: str = f.readline().split(":")[1].lstrip()
    distances_str: str = f.readline().split(":")[1].lstrip()

    t: int = int(times_str.replace(" ", ""))
    d: int = int(distances_str.replace(" ", ""))

    result: int = 1

    least_held_button_win: int = next(
        held_t for held_t in range(t) if (t - held_t) * held_t > d
    )
    most_held_button_win: int = (
        next(held_t for held_t in range(t, -1, -1) if (t - held_t) * held_t > d) + 1
    )

    print(
        f"least is {least_held_button_win} and most is {most_held_button_win} for {t}, {d} leaving {most_held_button_win-least_held_button_win} possible wins"
    )

    result *= most_held_button_win - least_held_button_win

    print(result)
