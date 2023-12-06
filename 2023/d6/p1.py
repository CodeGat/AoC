import re

with open('./2023/d5/in.txt') as f:
    times_str: str = f.readline().split(':')[1].lstrip()
    distances_str: str = f.readline().split(':')[1].lstrip()
    times: list[str] = re.split('\s+', times_str)
    distances: list[str] = re.split('\s+', distances_str)
    time_distance_pairs: list[tuple[int, int]] = [(int(t), int(d)) for t, d in zip(times, distances)]

    for time, distance in time_distance_pairs:
        least_held_button_win: int = next(held_t for held_t in range(time) if )
        most_held_button_win: int = get_winning_most_held_button(time, distance)