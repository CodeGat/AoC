from ast import mod
import re

nums: dict[str, int] = {
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
    for ix, line in enumerate(inp):
        f_modified_line: str = line.rstrip()
        r_modified_line: str = f_modified_line[::-1]

        pattern: str = "one|two|three|four|five|six|seven|eight|nine"
        f_pattern = re.compile(f"({pattern})")
        r_pattern = re.compile(f"({pattern[::-1]})")

        f_matches = f_pattern.findall(f_modified_line)
        if len(f_matches) != 0:
            f_modified_line = f_pattern.sub(str(nums[f_matches[0]]), f_modified_line, 1)

        r_matches = r_pattern.findall(r_modified_line)
        if len(r_matches) != 0:
            r_modified_line = r_pattern.sub(
                str(nums[r_matches[0][::-1]]), r_modified_line, 1
            )

        total += int(
            next(ch for ch in f_modified_line if ch.isdigit())
            + next(ch for ch in r_modified_line if ch.isdigit())
        )

print(f"-------------------\n{total}")
