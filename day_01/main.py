import string


def part_one(line: string) -> int:
    first_digit = next(char for char in line if char.isdigit())
    last_digit = next(char for char in reversed(line) if char.isdigit())
    return int(str(first_digit) + str(last_digit))


def part_two_prepare(line: string) -> string:
    word_list = {
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
    for key, value in word_list.items():
        if key in line:
            line = line.replace(key, key[0] + str(value) + key[-1])
    return line


def part_two(line: string) -> int:
    return part_one(part_two_prepare(line))


if __name__ == '__main__':
    partOneResult = 0
    partTwoResult = 0
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            partOneResult += part_one(line)
            partTwoResult += part_two(line)

    print("Part One: " + str(partOneResult))
    print("Part Two: " + str(partTwoResult))
