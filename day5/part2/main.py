def ocean_floor2(textfile):
    import numpy as np
    import matplotlib.pyplot as plt

    # Read the input data
    data = np.array([[list(map(int, s.split(','))) for s in l.split(' -> ')] 
                        for l in open(textfile, "r").read().splitlines()], 
                        ndmin=2, dtype=np.uint16)

    # Initialize ocean floor
    M = np.zeros((1000, 1000), dtype=np.uint8)


    for m in data:

        rows = m[:, 1]
        columns = m[:, 0]

        dir_rows = 1 if rows[1] >= rows[0] else -1
        dir_columns = 1 if columns[1] >= columns[0] else -1

        row_range = np.arange(rows[0], rows[1]+dir_rows, dir_rows, dtype=np.uint16)
        column_range = np.arange(columns[0], columns[1]+dir_columns, dir_columns, dtype=np.uint16)

        # Add to the ocean floor
        M[row_range, column_range] += 1
        
    plt.imshow(M)  # just for fun
    plt.savefig("ocean_floor2.png", dpi=300)
    plt.show()

    return (M >= 2).sum()


print(ocean_floor2(textfile="input.txt"))
