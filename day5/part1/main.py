def ocean_floor(textfile):
    import numpy as np
    import matplotlib.pyplot as plt

    # Read the input data
    data = np.array([[list(map(int, s.split(','))) for s in l.split(' -> ')] 
                        for l in open(textfile, "r").read().splitlines()], 
                        ndmin=2, dtype=np.uint16)

    # Initialize ocean floor
    M = np.zeros((1000, 1000), dtype=np.uint8)

    for m in data:
        
        # Check condition of horizontal or vertical lines
        if (m[0] == m[1]).any():
            
            rows = sorted(m[:, 1])
            columns = sorted(m[:, 0])

            # Add to the ocean floor
            M[rows[0]:rows[1]+1, columns[0]:columns[1]+1] += 1

    plt.imshow(M)  # just for fun
    plt.savefig("ocean_floor.png", dpi=300)
    plt.show()

    return (M >= 2).sum()

print(ocean_floor(textfile="input.txt"))
