lines = open("input.txt").read().splitlines()
closer = {"(": ")", "[": "]", "{": "}", "<": ">"}

def get_stack(line):
    stack = list()
    corrupted = False
    
    for char in line:
        if closer.get(char, False):  # If beginning of chunk
            stack.append(char)  # Add to stack
        else:  # If end of chunk
            if closer[stack[-1]] != char:
                corrupted = True
            else:
                del stack[-1]
    if not corrupted:
        return stack
        
stacks = list()
for line in lines:
    stack = get_stack(line)
    if stack: stacks.append(stack)
completions = [list(map(lambda x: closer[x], stack[::-1])) for stack in stacks]
close_scores = {")": 1, "]": 2, "}": 3, ">": 4}
totals = list()
for completion in completions:
    total = 0
    for char in completion:
        total *= 5
        total += close_scores[char]
    totals.append(total)

print(sorted(totals)[len(totals) // 2])
