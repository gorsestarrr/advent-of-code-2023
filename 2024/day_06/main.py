from enum import Enum


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


rotation_map = {
    Direction.UP: Direction.RIGHT,
    Direction.RIGHT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT,
    Direction.LEFT: Direction.UP,
}

moving_map = {
    Direction.UP: (-1, 0),
    Direction.RIGHT: (0, 1),
    Direction.DOWN: (1, 0),
    Direction.LEFT: (0, -1)
}


def part1(matrix):
    position = next((i, j) for i, row in enumerate(matrix) for j, char in enumerate(row) if char == '^')
    direction = Direction.UP
    rows, cols = len(matrix), len(matrix[0])
    steps_taken = {position}
    while True:
        x_current, y_current = position
        new_position = (x_current + moving_map[direction][0], y_current + moving_map[direction][1])
        x_new, y_new = new_position
        if not (0 <= x_new < rows and 0 <= y_new < cols):
            break
        if matrix[x_new][y_new] == '#':
            direction = rotation_map[direction]
        else:
            position = new_position
            steps_taken.add(position)
    print(len(steps_taken))


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        matrix = [list(line) for line in file.read().strip().split('\n')]
        part1(matrix)
