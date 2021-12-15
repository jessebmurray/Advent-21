data = [entry.split('-') for entry in open("input.txt").read().splitlines()]
connections = {vertex: list() for vertex in set(vertex for pair in data for vertex in pair)}
for pair in data: connections[pair[0]].append(pair[1]); connections[pair[1]].append(pair[0])
stack, paths = ["start"], list()

def travel():
    for connection in connections[stack[-1]]:
        if connection.islower() and connection in stack: pass
        elif connection == "end": paths.append(stack + [connection])
        else: stack.append(connection); travel()
    del stack[-1]

travel()
print(sum([any(map(lambda vertex: vertex.islower(), path[1:-1])) for path in paths]))
