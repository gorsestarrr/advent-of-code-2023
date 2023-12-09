def part1(seqs):
    return sum(extrapolate_forward(seq) for seq in seqs)


def part2(seqs):
    return sum(extrapolate_backwards(seq) for seq in seqs)


def extrapolate_forward(seq):
    if sum(seq) == 0:
        return 0
    return seq[-1] + extrapolate_forward([j - i for i, j in zip(seq[:-1], seq[1:])])


def extrapolate_backwards(seq):
    if sum(seq) == 0:
        return 0
    return seq[0] - extrapolate_backwards([j - i for i, j in zip(seq[:-1], seq[1:])])


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        seqs = [list(map(int, line.split())) for line in lines]
        print(part1(seqs))
        print(part2(seqs))
