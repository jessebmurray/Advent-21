def manhattan_plus_euclidean(textfile):
    """
    We know the sum of an additive series from 1 to n is n(n+1)/2. 
    Therefore, for distance d, the fuel cost is d(d+1)/2 = 1/2 (d^2 + d).
    We see that the cost function penalizes an equal weighting of the squared distance 
    and the absolute distance. Therefore, the total cost, which is the sum of the costs,
    is an equal weighting of the L2 and L1 norms from the alignment position. These are 
    individually minimized by the mean and median, respectively. We can imagine a weighting 
    such as cost = a*L2 + (1-a)*L1. As a shifts from 0 to 1, the argmin (alignment position)
    shifts from the mean to the median. We conclude that the optimal position must be between
    the mean and median and can reduce the search space to these points. It is also easy to 
    vectorize the L2 and L1 norm penalties. 
    """
    import numpy as np

    nums = np.array([int(n) for n in open(textfile, "r").read().split(',')], dtype=int)

    median = int(np.quantile(nums, 0.5))
    mean_r = int(np.round(np.mean(nums)))  # rounded mean

    search = [median, mean_r]  # define the boundaries of the search range
    search.sort()
    search[1] += 1
    search_range = np.arange(*search).reshape(-1, 1)

    # Get the cost for each position in the search range as an array
    costs = (np.sum(np.square(nums - search_range) + np.abs(nums - search_range), axis=1, dtype=int)) // 2

    i = np.argmin(costs)  # Get the argmin

    position = search_range.ravel()[i]  # get the optimal alignment position
    cost = costs[i]  # get the optimal total fuel cost 

    print("Median:", median) 
    print("Rounded mean:", mean_r) 
    print("Optimal position and cost: ", position, ", ", cost, sep="")

    return cost


print(manhattan_plus_euclidean(textfile="input.txt"))
