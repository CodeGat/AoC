import numpy as np

with open("./2023/d10/in.txt") as f:
    pipe_map: np.ndarray = np.array([list(row.rstrip()) for row in f])
    start: list[int] = np.argwhere(pipe_map=='S')[0]
    print(start[0])
    # start: tuple[int, int] = next(((x, y) for y, row in enumerate(pipe_map) for x, pos in enumerate(row) if pos == 'S'))

    # first_pipe = look_around_for_next_pipe(start, pipe_map, return_on_found=False)