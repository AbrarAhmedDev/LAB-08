
warehouse = {
    "Receiving": {"Aisle1": 40, "Aisle2": 70},
    "Aisle1": {"Aisle2": 30, "Packing Station": 90},
    "Aisle2": {"Packing Station": 35},
    "Packing Station": {},
}

heuristic = {"Receiving": 100, "Aisle1": 70,"Aisle2": 35, "Packing Station": 0}


def get_g(path):
    total = 0
    for i in range(len(path) - 1):
        total = total + warehouse[path[i]][path[i + 1]]
    return total


def get_h(path):
    return heuristic[path[-1]]


def get_f(path):
    return get_g(path) + get_h(path)


def a_star(start, goal):
    frontier = [[start]]
    visited = []
    explored = 0  

    while len(frontier) > 0:
        frontier.sort(key=get_f)
        path = frontier.pop(0)
        node = path[-1]

        if node in visited:
            continue
        visited.append(node)
        explored = explored + 1  # (b)

        print("Exploring", node, " path:", path," g =", get_g(path), " h =", get_h(path), " f =", get_f(path))

        if node == goal:
            print()
            print("Path found by A*:", path)
            print("Total cost of this path:", get_g(path))
            print("Total nodes explored:", explored)  # (b)
            return path

        for neighbour in warehouse[node]:
            frontier.append(path + [neighbour])

    return None


a_star("Receiving", "Packing Station")
