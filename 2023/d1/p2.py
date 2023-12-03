nums: dict[int, str] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
total: int = 0

with open("./2023/d1/in.txt", "r") as inp:
    for line in inp:
        replaced_line: str = ""
        token: str = ""
        nums_matching_this_token: dict[str, int] = nums.copy()

        for ch in line:
            token += ch

            # Case 1: it is a digit, move on
            if ch.isdigit():
                replaced_line += token
                token = ""
                nums_matching_this_token = nums.copy()
                continue

            keys: list[str] = list(nums_matching_this_token.keys())

            for key in keys:
                if not key.startswith(token):
                    nums_matching_this_token.pop(key)

            if len(nums_matching_this_token) == 0:
                token = ch
                nums_matching_this_token = nums.copy()

            if token in nums.keys():
                replaced_line += str(nums.get(token, token))
                token = ""
                nums_matching_this_token = nums.copy()

        nums_matching_this_token = nums.copy()

        print(replaced_line)

        total += int(
            next(ch for ch in replaced_line if ch.isdigit())
            + next(ch for ch in reversed(replaced_line) if ch.isdigit())
        )

print(f"-------------------\n{total}")
