def play_bingo(textfile):
    import numpy as np

    input = open(textfile, "r").read().split("\n\n")

    nums = np.array([int(n) for n in input[0].split(",")], dtype=np.uint8)

    arrays = list()
    for j in range(1, len(input)):
        arrays.append(np.array([[int(n) for n in nums.split()] for nums in input[j].splitlines()], dtype=np.uint8))

    shape = arrays[0].shape
    N = len(arrays)

    bols = list()
    for j in range(N):
        bols.append(np.full(shape, False, dtype=np.bool8))

    def check_arrays(num):
        for j in range(N):
            
            array = arrays[j]
            bol = bols[j]

            # Update board
            bol += array == num
        
            # Check for win condition
            if np.array([bol.all(axis=0).any(), bol.all(axis=1).any()]).any():
                # If so return unmarked numbers sum times number
                return (~bol * array).sum() * num, array, bol, num

    
    for num in nums:
        check = check_arrays(num)
        
        if check:
            return check


print(play_bingo(textfile="input.txt"))
