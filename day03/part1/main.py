def fast(textfile):
    import numpy as np
    data = np.array([[bool(int(v)) for v in l.rstrip('\n')] for l in open(textfile)])
    g = data.sum(axis=0) > data.shape[0] / 2
    e = ~g
    def convert(array):
        return int(''.join(list(map(lambda x: str(int(x)), array))), 2)
    return convert(g) * convert(e)

print(fast(textfile="input.txt"))