import itertools


def generate_combinations(n, array):
    return [list(combination) for combination in itertools.product(array, repeat=n)]


def part1(equations):
    sum = 0
    for equation in equations:
        target, numbers = equation
        operators = generate_combinations(len(numbers), [0, 1])  # 0 -> +, 1 -> *
        for operator in operators:
            execution = numbers[0]
            for index, number in enumerate(numbers[1:], start=1):
                if operator[index - 1] == 0:
                    execution += number
                else:
                    execution *= number
            if execution == target:
                sum += execution
                break
    return sum

def part2(equations):
    sum = 0
    for equation in equations:
        target, numbers = equation
        operators = generate_combinations(len(numbers), [0, 1, 2])  # 0 -> +, 1 -> *, 2 -> ||
        for operator in operators:
            execution = numbers[0]
            for index, number in enumerate(numbers[1:], start=1):
                if operator[index - 1] == 0:
                    execution += number
                elif operator[index - 1] == 1:
                    execution *= number
                else:
                    execution = int(str(execution) + str(number))

            if execution == target:
                sum += execution
                break
    return sum


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    equations = []
    for line in lines:
        target, numbers = line.strip().split(':')
        equations.append((int(target), list(map(int, numbers.strip().split()))))
    print(part1(equations))
    print(part2(equations))
