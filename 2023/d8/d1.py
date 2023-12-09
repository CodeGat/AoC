import re

with open('./2023/d8/in.txt') as f:
    instructions: str = f.readline().rstrip()
    f.readline()

    network_comps: list[tuple] = [tuple(re.split(' = \(|, |\)\n', line)[:3]) for line in f]
    network: dict[str, tuple[str, str]] = {n: (l, r) for n, l, r in network_comps}

    steps: int = 0
    instruction: int = 0
    node: str = 'AAA'

    while node != 'ZZZ':
        node = network[node][0 if instructions[instruction] == 'L' else 1]
        steps += 1
        instruction = (instruction + 1) % len(instructions)

    print(steps)