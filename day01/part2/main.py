def brutus(textfile):
    """This code would be necessary if the operator wasn't a rolling sum but 
    instead something non-linear. But with the operator being addition, it's
    knowingly quite brute."""

    counter = 0
    j = 1
    abc = [None] * 3
    
    for l in open(textfile):

        current = int(l)
        
        # Initialize or reset last bin
        abc[(j-1) % 3] = 0


        # Add to all bins, if initialized
        for i in range(3):
            try: 
                abc[i] += current
            except TypeError:  
                # can't add to NoneType
                pass


        # Make comparison
        # Get current bin (we reset this next loop)
        current_sum = abc[j]
        try:
            # compare it to the last sum
            counter += current_sum > last_sum
        except:
            pass
        # it will be the next sum compared against
        last_sum = current_sum

        # Move the bin forward by one
        j = (j + 1) % 3


    return counter




print(brutus(textfile="input.txt"))

