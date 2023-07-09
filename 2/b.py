def h(n):
    H = {'A': 3, 'B': 4, 'C': 2, 'D': 6, 'G': 0, 'S': 5}
    return H[n]

def a_star_algorithm(graph, start, goal):

    open_list = [start]
    closed_list = set()

    g = {start:0}

    parents = {start:start}

    while open_list:

        open_list.sort(key=lambda v: g[v] + h(v), reverse=True)
        n = open_list.pop()

        # If node is goal then construct the path and return
        if n == goal:
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start)
            reconst_path.reverse()

            print(f'Path found: {reconst_path}')
            return reconst_path

        for (m, weight) in graph[n]:
        # if m is first visited, add it to open_list and note its parent
            if m not in open_list and m not in closed_list:
                open_list.append(m)
                parents[m] = n
                g[m] = g[n] + weight

            # otherwise, check if it's quicker to first visit n, then m
            # and if it is, update parent and g data
            # and if the node was in the closed_list, move it to open_list
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.append(m)

        # Node's neighbours are visited. Now put node to closed list.
        closed_list.add(n)

    print('Path does not exist!')
    return None


graph = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3),('G', 4)],
    'D': [('G', 2)]
}

a_star_algorithm(graph, 'S', 'G')