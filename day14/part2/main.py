import itertools

template, insertion_rules = open("input.txt").read().split("\n\n")
insertion_rules = {pair: insertion for pair, insertion in map(lambda l: l.split(" -> "), insertion_rules.splitlines())}
unique_letters = list(set(''.join([item for pair in insertion_rules.items() for item in pair]) + template))
counts = {''.join(pair): template.count(''.join(pair)) for pair in itertools.product(unique_letters, repeat=2)}

def polymerize_once(counts):
    next_counts = counts.copy()
    for pair in insertion_rules.keys():
        (left, right), insertion = pair, insertion_rules[pair]

        next_counts[left + insertion] += counts[pair]
        next_counts[insertion + right] += counts[pair]
        next_counts[pair] -= counts[pair]
    return next_counts

def polymerize(counts, n_steps=1): 
    for _ in range(n_steps): counts = polymerize_once(counts)
    return counts

def get_single_counts(counts):
    single_counts = {letter: 1 if letter == template[0] else 0 for letter in unique_letters}
    for letter in unique_letters:
        for pair, count in list(counts.items()):
            if letter == pair[1]: single_counts[letter] += count
    return single_counts

def part2(): return sum(map(lambda g: g[0] * single_counts[g[1](single_counts, key=single_counts.get)], ((1, max), (-1, min))))

counts = polymerize(counts, n_steps=40)
single_counts = get_single_counts(counts)
print(part2())
