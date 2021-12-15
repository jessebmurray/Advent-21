import numpy as np
import matplotlib.pyplot as plt

paper, instructions = open("input.txt").read().split('\n\n')
instructions = [instruction.split()[-1] for instruction in instructions.splitlines()]
instructions = [[instruction.split("=")[0], int(instruction.split("=")[1])] for instruction in instructions]
locs = np.array([list(map(int, pair.split(',')))[::-1] for pair in paper.splitlines()], dtype=np.uint16)

X = np.zeros(shape=(9999, 9999), dtype=bool)
rows, cols = locs.T
X[rows, cols] = True

n_dots = list()
for kind, f in instructions:
    if kind == 'x': X = X[:,:f] | X[:,2*f:f:-1]
    else: X = X[:f] | X[2*f:f:-1]
    n_dots.append(X.sum())

print(n_dots[0])
plt.imshow(X)
plt.savefig("letters.png", dpi=300)
