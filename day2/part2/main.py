
def simple(textfile):
    position = 0
    depth = 0
    aim = 0
    for j in open(textfile):
        movement, amount = j.split()
        amount = int(amount)
        print
        if movement== "forward":
            position += amount
            depth = depth + (aim * amount)
        elif movement == "up":
            aim -= amount
        elif movement == "down":
            aim += amount
    
    return depth * position

print(simple(textfile="input.txt"))

