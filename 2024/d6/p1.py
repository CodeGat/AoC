from enum import Enum

class Guard():
    def __init__(self, map: list[list[str]]):
        self.map: list[list[str]] = map
        found_x, found_y = self._find_initial()
        self.x = found_x
        self.y = found_y
        self.dir = "UP"
        self.is_on_map = True

    def _find_initial(self) -> tuple[int, int]:
        for i in range(len(map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == '^':
                    return j, i
        raise Exception("Couldn't find the guard")

    def change_dir(self) -> str:
        if self.dir == "UP":
            self.dir = "LEFT"
        elif self.dir == "LEFT":
            self.dir = "DOWN"
        elif self.dir == "DOWN":
            self.dir = "RIGHT"
        elif self.dir == "RIGHT":
            self.dir = "UP"
        else:
            raise Exception

        return self.dir

    def walk_until_obstacle(self):
        # set self.off_map if we get out of bounds
        x = self.x
        y = self.y
        has_hit_obstacle = False

        while self.is_on_map:
            self.map[y][x] = "X"

            if self.dir == "UP":
                y -= 1
            elif self.dir == "LEFT":
                x += 1
            elif self.dir == "DOWN":
                y += 1
            elif self.dir == "RIGHT":
                x -= 1

            if x == -1 or x == len(self.map[0]) or y == -1 or y == len(self.map):
                self.is_on_map = False
            elif self.map[y][x] == "#":
                break
            else:
                self.map[y][x] = "G"
                self.x = x
                self.y = y

with open("./2024/d6/in.txt") as f:
    map: list[list[str]] = [list(row.strip()) for row in f.readlines()]

    guard = Guard(map)

    while guard.is_on_map:
        guard.walk_until_obstacle()
        print("BONK!")
        guard.change_dir()

    print(sum(row.count('X') for row in map))
