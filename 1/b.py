def best_first_search(graph,start,goal):
    open_list = [(0,start)]
    closed_list = set()
    while open_list:
        open_list.sort(reverse=True)
        cost, node = open_list.pop()
        
        if node in closed_list:
            continue

        if node==goal:
            return cost

        closed_list.add((cost,node))
        for neighbour, neighbour_cost in graph[node]:
            if neighbour not in closed_list and neighbour not in closed_list:
                open_list.append((neighbour_cost+cost, neighbour))

    return None


graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1)],
    'C': []
}

start = input("Start node: ")
goal = input("Goal node: ")

result = best_first_search(graph, start, goal)

if result:
    print(f"The minimum cost from {start} to {goal} is {result}")
else:
    print(f"No path from {start} to {goal}")
