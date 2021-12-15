def fast2(textfile):
    import numpy as np
    
    data = np.array([[bool(int(v)) for v in l.rstrip('\n')] for l in open(textfile)])

    def get_rating(data, rating):
        import operator

        ops = {"oxygen": operator.ge,
                "CO2": operator.lt}

        i = 0
        n = data.shape[0]


        while n > 1:
            
            c = ops[rating](data[:, i].sum(), n / 2)

            data = data[data[:, i] == c]

            # Update n and i
            n = data.shape[0]
            i += 1
        
        return data.ravel()

    oxygen_rating, co2_rating = get_rating(data, "oxygen"), get_rating(data, "CO2")


    def convert(array):
        return int(''.join(list(map(lambda x: str(int(x)), array))), 2)
    
    return convert(oxygen_rating) * convert(co2_rating)

print(fast2("input.txt"))
