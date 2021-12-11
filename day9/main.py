import numpy as np
import matplotlib.pyplot as plt


def get_X(textfile):
    return np.array([[int(n) for n in line] for line in open(textfile, "r").read().splitlines()], dtype=np.uint8)


def get_low(X):  # Get low points
    L, R = np.pad(X[:, :-1], [(0, 0), (1, 0)], constant_values=10), np.pad(X[:, 1:], [(0, 0), (0, 1)], constant_values=10)
    T, B = np.pad(X[:-1, :], [(1, 0), (0, 0)], constant_values=10), np.pad(X[1:, :], [(0, 1), (0, 0)], constant_values=10)
    return (X < L) * (X < R) * (X < T) * (X < B)


def padding(textfile):  # Part 1 solution
    X = get_X(textfile=textfile)
    P = get_low(X)
    plt.imshow(P)  # Just for fun
    plt.savefig("low_points.png", dpi=300)
    return np.sum(X[P] + 1)


def slicing(textfile):  # Part 2 solution
    X = get_X(textfile)
    P = get_low(X)
    n_low = np.sum(P)

    slices = {"L": (slice(None, None), slice(None, -1)), "R": (slice(None, None), slice(1, None)), 
              "T": (slice(None, -1), slice(None, None)), "B": (slice(1, None), slice(None, None))}
    dirs = [("L", "R"), ("R", "L"), ("T", "B"), ("B", "T")]

    M = np.zeros(shape=X.shape, dtype=np.int16)
    M[P] = np.arange(1, n_low + 1)
    M[X == 9] = -1

    def transfer(receive_dir, give_dir):
        receive, give = M[slices[receive_dir]], M[slices[give_dir]]
        available, marked = (receive == 0), (give > 0)
        idx = available * marked
        receive[idx] = give[idx]

    while (M == 0).any():
        for dir in dirs:
            transfer(*dir)
        
    plt.imshow(M)  # Just for fun    
    plt.savefig("numbered_basins.png", dpi=300)

    sizes = np.array([np.sum(M == j) for j in range(1, n_low + 1)], dtype=np.uint16)
    return np.product(sizes[np.argpartition(sizes, -3)[-3:]])


print("Part 1:", padding(textfile="input.txt"))
print("Part 2:", slicing(textfile="input.txt"))
