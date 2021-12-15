data = [entry.split('-') for entry in open("input.txt").read().splitlines()]
connections = {vertex: list() for vertex in set(vertex for pair in data for vertex in pair)}
lowers = list(filter(lambda x: x.islower() and x not in ('start', 'end'), connections.keys()))
for pair in data: connections[pair[0]].append(pair[1]); connections[pair[1]].append(pair[0])
stack, paths = ["start"], list()

def travel():
    for connection in connections[stack[-1]]:
        if connection == "start": pass
        elif connection.islower() and connection in stack and max(map(lambda lower: stack.count(lower), lowers)) == 2: pass
        elif connection == "end": paths.append(stack + [connection])
        else: stack.append(connection); travel()
    del stack[-1]

travel()
print(len(paths))
