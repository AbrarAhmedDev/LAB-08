graph = {
    "S": {"A": 6, "B": 5, "C": 10},
    "A": {"E": 6},
    "B": {"E": 6, "D": 7},
    "C": {"D": 6},
    "D": {"F": 6},
    "E": {"F": 4},
    "F": {"G": 3},
    "G": {},
}

heuristic = {"S": 17, "A": 10, "B": 13, "C": 4,"D": 2, "E": 4, "F": 1, "G": 0}

def get_g(path):
    total = 0
    for i in range(len(path) - 1):
        total = total + graph[path[i]][path[i + 1]]
    return total

def get_h(path):
    return heuristic[path[-1]]

def get_f(path):
    return get_g(path) + get_h(path)

def a_star(start, goal):
    frontier = [[start]]
    explored = 0  

    while len(frontier) > 0:
        frontier.sort(key=get_f)
        path = frontier.pop(0)
        node = path[-1]
        explored = explored + 1  

        print("Exploring", node, " path:", path," g =", get_g(path), " h =", get_h(path), " f =", get_f(path))

        if node == goal:
            print()
            print("Path found by A*:", path)
            print("Total cost of this path:", get_g(path))
            print("Total nodes explored:", explored)  # (b)
            return path

        for neighbour in graph[node]:
            frontier.append(path + [neighbour])

    return None


a_star("S", "G")
