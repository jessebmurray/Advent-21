def check_all(part, textfile):

    import itertools; import string; import numpy as np

    assert part in [1, 2]

    data = [list(map(lambda y: list(map(lambda x: ''.join(sorted(x)), y)), map(lambda x: x.split(), entry.split('|')))) for entry in open(textfile, "r").read().splitlines()]

    locs = {0: [0, 1, 2, 4, 5, 6], 1: [2, 5], 2: [0, 2, 3, 4, 6], 3: [0, 2, 3, 5, 6], 4: [1, 2, 3, 5], 5: [0, 1, 3, 5, 6], 6: [0, 1, 3, 4, 5, 6], 7: [0, 2, 5], 8: [0, 1, 2, 3, 4, 5, 6], 9: [0, 1, 2, 3, 5, 6]}

    permutations = [{''.join(sorted(permutation[locs[i]])): i for i in range(10)} for permutation in np.array(list(itertools.permutations([l for l in string.ascii_lowercase[:7]])))]

    NUMS = np.zeros(shape=(len(data), 4), dtype=int)

    for j in range(len(data)):
        for i in range(len(permutations)):
            if set(data[j][0]) == set(permutations[i].keys()):
                break
        NUMS[j] = [permutations[i][string] for string in data[j][1]]
        
        
    return sum([(NUMS == digit).sum() for digit in [1, 4, 7, 8]]) if part == 1 else sum([int(''.join(map(str, num))) for num in NUMS])


print(check_all(part=1, textfile="input.txt"))

print(check_all(part=2, textfile="input.txt"))
