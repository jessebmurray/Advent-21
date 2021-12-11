def lad(textfile):
    """
    It is a well known fact that the median minimizes the least absolute deviations. 
    We therefore select the median to be the alignment position.
    We then calculate the sum of the absolute deviations from this position.
    """
    import numpy as np
    nums = np.array([int(n) for n in open(textfile, "r").read().split(',')], dtype=int)
    median = int(np.quantile(nums, 0.5))
    return np.sum(np.abs(nums - median))

print(lad(textfile="input.txt"))
