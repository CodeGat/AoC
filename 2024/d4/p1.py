import itertools

def check_surrounds_for_string(crossword: list[list[str]], row: int, col: int, find: str) -> int:
    find_rest: str = find[1:]
    number_of_string_in_surrounds: int = 0

    for add_row, add_col in itertools.product(range(-1, 2), repeat=2):
        if check_for_string(crossword, row, col, add_row, add_col, find_rest) != 0:
            number_of_string_in_surrounds += 1

    return number_of_string_in_surrounds

def check_for_string(crossword: list[list[str]], row: int, col: int, add_row: int, add_col: int, find: str) -> bool:
    if find == "":
        print("Found it!!")
        return True

    new_row: int = row + add_row
    new_col: int = col + add_col

    print(f"Checking {find}: From {row},{col} (adding {add_row},{add_col}) to {new_row},{new_col}")

    if new_col == -1 or new_col == len(crossword) or new_row == -1 or new_row == len(crossword[0]):
        return False

    if crossword[new_row][new_col] == find[0]:
        return check_for_string(crossword, new_row, new_col, add_row, add_col, find[1:])
    else:
        return False

with open("./2024/d4/in.txt") as f:
    crossword: list[list[str]] = [list(row.strip()) for row in f.readlines()]
    result: int = 0

    row_length: int = len(crossword)
    col_length: int = len(crossword[0])

    string_to_find: str = "XMAS"

    for row in range(row_length):
        for col in range(col_length):
            print(f"Attempting ({row}, {col}): {crossword[row][col]}")
            if crossword[row][col] == 'X':
                result += check_surrounds_for_string(crossword, row, col, string_to_find)

    print(result)

