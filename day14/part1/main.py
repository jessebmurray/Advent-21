template, insertion_rules = open("input.txt").read().split("\n\n")
insertion_rules = {pair: insertion for pair, insertion in map(lambda l: l.split(" -> "), insertion_rules.splitlines())}

def iterate(current_node):
    next_node = current_node.points_to
    if next_node:
        insert_letter = insertion_rules.get(current_node.letter + next_node.letter, False)
        if insert_letter:
            new_node = Node(insert_letter)
            current_node.points_to, new_node.points_to = new_node, next_node
        iterate(next_node)

class Node:
    def __init__(self, letter): self.letter, self.points_to = letter, None
    def __str__(self): return self.letter
        
class Polymer:
    def __init__(self, template, recursion_limit=10_000):
        self.start_node, self.string, self.recursion_limit = Node(template[0]), template, recursion_limit
        current_node = self.start_node
        for letter in template[1:]: current_node.points_to = Node(letter); current_node = current_node.points_to

    def __str__(self): return self.string
    def __len__(self): return len(self.string)
    def __getitem__(self, index): return self.string[index]

    @property
    def part1(self): return sum(map(lambda g: g[0] * self.string.count(g[1](self.string, key=self.string.count)), ((1, max), (-1, min))))

    def update_string(self):
        current_node, self.string = self.start_node, self.start_node.letter
        while current_node.points_to: current_node = current_node.points_to; self.string += current_node.letter
        
    def polymerize(self, n_steps=1): 
        import sys
        original_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(self.recursion_limit)
        try:
            for _ in range(n_steps): iterate(current_node=self.start_node)
        except RecursionError:
            raise RecursionError('Increase `recursion_limit` parameter.')
        sys.setrecursionlimit(original_limit)
        self.update_string()
        

polymer = Polymer(template)
polymer.polymerize(n_steps=10)
print(polymer.part1)
