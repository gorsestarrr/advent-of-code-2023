import math
import re
from functools import reduce


def parse(all_data_lines):
    directions = all_data_lines[0].replace('L', '0').replace('R', '1').strip()
    tuples = {}
    pattern = re.compile(r'(\w+)\s*=\s*\(([^)]+)\)')
    for line in all_data_lines:
        match = pattern.match(line.strip())
        if match:
            tuples[match.group(1)] = tuple(map(str.strip, match.group(2).split(',')))
    return directions, tuples


def solve_one(direction, dict, start_from, ends_with):
    steps = index = 0
    current = dict[start_from]
    position = current[int(direction[index])]
    while not position.endswith(ends_with):
        position = current[int(direction[index])]
        current = dict[position]
        index = (index + 1) % len(direction)
        steps += 1
    return steps


def part1(direction, dict):
    return solve_one(direction, dict, 'AAA', 'ZZZ')


def part2(direction, dict):
    return reduce(math.lcm, [solve_one(direction, dict, key, 'Z') for key in [key for key in dict.keys() if key.endswith('A')]])

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        direction, dict = parse(file.readlines())
        rv1 = part1(direction, dict)
        print(rv1)
        rv2 = part2(direction, dict)
        print(rv2)
