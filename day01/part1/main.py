def one_loop(textfile):
    
    counter = 0
    
    for l in open(textfile):
        current = int(l)
        try:
            counter += current > last
        except UnboundLocalError:  # There is no 'last' for the first entry
            pass
        last = current  

    return counter

print(one_loop(textfile="./input.txt"))
