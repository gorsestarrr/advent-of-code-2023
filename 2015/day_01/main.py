def part_one(line):
    return sum(1 if char == '(' else -1 for char in line)


def part_two(line):
    floor = 0
    for i, char in enumerate(line):
        floor += 1 if char == '(' else -1
        if floor == -1:
            return i + 1
    return None


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        line = file.readline()
        print(part_one(line))
        print(part_two(line))
