def lantern_counts(n_days, textfile):
    import matplotlib.pyplot as plt

    nums = [int(n) for n in open(textfile, "r").read().split(',')]

    # d contains the count of lanternfish with timer value j
    d = {j: 0 for j in range(9)}

    # Initialize d to data
    for j in nums:
        d[j] += 1

    def update():
        
        n_doubled = d[0]
        
        for j in range(8):
            d[j] = d[j+1]

        d[8] = n_doubled
        d[6] += n_doubled
        

    for j in range(n_days):
        update()

    # For fun
    plt.bar(list(d.keys()), list(d.values()))
    plt.xlabel("Timer Value") 
    plt.ylabel("Number of Lanternfish")
    plt.savefig("n_each.png", dpi=300)
    plt.show()


    return sum(d.values())


print(lantern_counts(n_days=256, textfile="input.txt"))
