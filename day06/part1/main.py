def lanternfish(n_days, textfile):
    
    nums = [int(n) for n in open(textfile, "r").read().split(',')]

    def loop():
        N = len(nums)
        add_N = 0
        for i in range(N):
            if nums[i] == 0:
                add_N += 1
                nums[i] = 6
            else:
                nums[i] -= 1

        for i in range(add_N):
            nums.append(8)

    for j in range(n_days):
        loop()

    return len(nums)


print(lanternfish(n_days=80, textfile="input.txt"))
