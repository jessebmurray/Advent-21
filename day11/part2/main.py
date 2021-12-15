def get_critical_step(textfile):
    import numpy as np
    slices = {"L": (slice(None, None), slice(None, -1)), "R": (slice(None, None), slice(1, None)), 
                "T": (slice(None, -1), slice(None, None)), "B": (slice(1, None), slice(None, None))}
    slices = slices | {loc: (slices[loc[0]][0], slices[loc[1]][1]) for loc in ["TL", "TR", "BL", "BR"]}
    loc_pairs = [("L", "R"), ("T", "B"), ("BR", "TL"), ("BL", "TR")]
    X = np.array([list(map(int, l.strip())) for l in open(textfile)], dtype=np.uint8)
    n_flashes = 0

    def iterate(X, n_flashes):
        F = np.zeros(shape=X.shape, dtype=bool)
        X += 1
        while (X > 9).any():
            M = (X > 9)
            F = F | M
            for loc_pair in loc_pairs:
                X[slices[loc_pair[0]]] += M[slices[loc_pair[1]]]
                X[slices[loc_pair[1]]] += M[slices[loc_pair[0]]]
            X[F] = 0
        n_flashes += F.sum()
        all_flash = F.sum() == X.size
        return X, n_flashes, all_flash

    i = 1
    while True:
        X, n_flashes, all_flash = iterate(X, n_flashes)
        if all_flash: return i
        i += 1

print(get_critical_step(textfile="input.txt"))
