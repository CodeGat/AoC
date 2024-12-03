import re


with open("./2024/d3/in.txt") as f:
    program: str = "".join(f.readlines())
    result: int = 0

    valid_mul_regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    valid_muls_in_program = re.findall(valid_mul_regex, program)
    print(valid_muls_in_program)

    for num1, num2 in valid_muls_in_program:
        result += int(num1) * int(num2)

    print(result)
