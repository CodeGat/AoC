import itertools

def check_surrounds_for_x_mas(crossword: list[list[str]], row: int, col: int) -> bool:

    # First check (-1,-1) of the current coord
    # TODO: functionalize the conditionals for less code smell
    new_row: int = row - 1
    new_col: int = col - 1
    opposite_row: int = row + 1
    opposite_col: int = col + 1

    # If we're out of bounds, exit
    if (
        new_col == -1
        or new_row == -1
        or opposite_col == len(crossword)
        or opposite_row == len(crossword[0])
    ):
        return False

    if not (
        (
            crossword[new_row][new_col] == "M"
            and crossword[opposite_row][opposite_col] == "S"
        )
        or (
            crossword[new_row][new_col] == "S"
            and crossword[opposite_row][opposite_col] == "M"
        )
    ):
        return False

    # Then check (-1, 1) of the current coord
    new_row: int = row - 1
    new_col: int = col + 1
    opposite_row: int = row + 1
    opposite_col: int = col - 1

    # If we're out of bounds, exit
    if (
        new_col == -1
        or new_row == -1
        or opposite_col == len(crossword)
        or opposite_row == len(crossword[0])
    ):
        return False

    if not (
        (
            crossword[new_row][new_col] == "M"
            and crossword[opposite_row][opposite_col] == "S"
        )
        or (
            crossword[new_row][new_col] == "S"
            and crossword[opposite_row][opposite_col] == "M"
        )
    ):
        return False

    return True


with open("./2024/d4/in.txt") as f:
    crossword: list[list[str]] = [list(row.strip()) for row in f.readlines()]
    result: int = 0

    for row in range(len(crossword)):
        for col in range(len(crossword[0])):
            print(f"Attempting ({row}, {col}): {crossword[row][col]}")
            if crossword[row][col] == "A" and check_surrounds_for_x_mas(
                crossword, row, col
            ):
                result += 1

    print(result)
