def play_bingo2(textfile):
    import numpy as np

    input = open(textfile, "r").read().split("\n\n")

    nums = np.array([int(n) for n in input[0].split(",")], dtype=np.uint8)

    arrays = list()
    for j in range(1, len(input)):
        arrays.append(np.array([[int(n) for n in nums.split()] for nums in input[j].splitlines()], dtype=np.uint8))

    shape = arrays[0].shape
    n_arrays = len(arrays)

    bols = list()
    for j in range(n_arrays):
        bols.append(np.full(shape, False, dtype=np.bool8))

    def check_arrays(num):
        j = 0
        while j < len(arrays):
            
            array = arrays[j]
            bol = bols[j]

            # Update board
            bol += array == num
        
            # Check for win condition
            if np.array([bol.all(axis=0).any(), bol.all(axis=1).any()]).any():
                
                # Check if it's the last board, if so, we're done
                if len(arrays) == 1:
                    return (~bol * array).sum() * num, array, bol, num
                else:
                    # If not, delete that board
                    del bols[j]
                    del arrays[j]
                    # We don't increase j because the boards have shifted down
            else:
                # If not a win condiiton, move to the next board
                j += 1

    
    for num in nums:
        check = check_arrays(num)
        
        if check:
            return check


print(play_bingo2("input.txt"))
