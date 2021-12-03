
def simple(textfile):
    position = 0
    depth = 0
    for l in open(textfile):
        l = l.split()
        if l[0] == "forward":
            position += int(l[1])
        elif l[0] == "up":
            depth -= int(l[1])
        elif l[0] == "down":
            depth += int(l[1])

    return position * depth


print(simple(textfile="input.txt"))
