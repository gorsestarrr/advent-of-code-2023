def parse(lines):
    graph, grid = {}, {}
    start = {0,0}
    for column, line in enumerate(lines):
        for row, char in enumerate(line.strip()):
            moves = {
                ".": [],
                "|": [(row, column - 1), (row, column + 1)],
                "-": [(row - 1, column), (row + 1, column)],
                "L": [(row, column - 1), (row + 1, column)],
                "J": [(row - 1, column), (row, column - 1)],
                "7": [(row - 1, column), (row, column + 1)],
                "F": [(row + 1, column), (row, column + 1)],
                "S": [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)],
            }
            # Remove moves with negative values
            filtered_moves = {key: [coord for coord in value if all(c >= 0 for c in coord)] for key, value in
                              moves.items()}
            graph[row, column] = filtered_moves[char]
            grid[row, column] = char
            if char == "S":
                start = (row, column)

    return graph, grid, start


def find_path(graph, start):
    path = [start]
    while path[-1] != start or len(path) < 2:
        current_node = path[-1]
        neighbors = []
        for neighbor in graph[current_node]:
            if neighbor not in path:
                neighbors.append(neighbor)
        if neighbors:
            next_node = neighbors[0]
            path.append(next_node)
        else:
            break
    return path


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        graph, grid, start = parse(lines)
        path = find_path(graph, start)
        print(len(path) // 2)
