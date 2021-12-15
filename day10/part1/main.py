lines = open("input.txt").read().splitlines()
closer = {"(": ")", "[": "]", "{": "}", "<": ">"}

def get_illegal(line):
    stack = list()
    
    for char in line:
        if closer.get(char, False):  stack.append(char)  # If beginning of chunk, add to stack
        else:  # If end of chunk
            if closer[stack[-1]] != char: return char
            else: del stack[-1]

scores = {")": 3, "]": 57, "}": 1197, ">": 25137, None: 0}
total = 0
for line in lines: total += scores[get_illegal(line)]

print(total)
