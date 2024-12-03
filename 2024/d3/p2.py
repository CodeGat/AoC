import re


with open("./2024/d3/in.txt") as f:
    program: str = "".join(f.readlines())
    result: int = 0

    do_command = re.compile(r"do\(\)")
    dont_command = re.compile(r"don't\(\)")
    mul_command = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    always_present_mul_tokens: int = len("mul(,)")

    counter: int = 0
    enabled_mul: bool = True

    print(program)

    while counter != len(program):
        print(f"At counter {counter} ({program[counter]}):")
        if program[counter] == 'd':  # start of a do/n't command
            print("Maybe a do/n't command:")
            if re.match(do_command, program[counter:]) is not None:
                enabled_mul = True
            elif re.match(dont_command, program[counter:]) is not None:
                enabled_mul = False
        elif program[counter] == 'm':  # start of a mul command
            print("Maybe a mul command:")
            mul_match = re.match(mul_command, program[counter:])
            if mul_match is not None:
                if enabled_mul:
                    print(f"mul command enabled, adding {mul_match} as {mul_match.group(1)}*{mul_match.group(2)}")
                    result += int(mul_match.group(1)) * int(mul_match.group(2))
                else:
                    print(f"mul command disabled, skipping {mul_match}")
                counter += always_present_mul_tokens + len(mul_match.group(1)) + len(mul_match.group(2))
                continue
        counter += 1

    print(result)
