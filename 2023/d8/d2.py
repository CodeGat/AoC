import re

with open('./2023/d8/in.txt') as f:
    instructions: str = f.readline().rstrip()
    f.readline()

    network_comps: list[tuple] = [tuple(re.split(' = \(|, |\)\n', line)[:3]) for line in f]
    network: dict[str, tuple[str, str]] = {n: (l, r) for n, l, r in network_comps}

    steps: int = 0
    instruction: int = 0
    nodes: list[str] = [n for n in network.keys() if n.endswith('A')]
    simultaneous_nodes: int = len(nodes)

    print(f"Starting with: {nodes}")

    while len([n for n in nodes if n.endswith('Z')]) != simultaneous_nodes:
        nodes = [network[node][0 if instructions[instruction] == 'L' else 1] for node in nodes]
        steps += 1
        instruction = (instruction + 1) % len(instructions)
        print(f'Now {nodes}')

    print(steps)
