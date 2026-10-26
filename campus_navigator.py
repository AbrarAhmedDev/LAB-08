
campus = {
    "Hostel": {"Cafeteria": 150, "Admin Block": 300},
    "Cafeteria": {"Academic Block": 200},
    "Admin Block": {"Academic Block": 120},
    "Academic Block": {"Library": 100},
    "Library": {},
}

heuristic = {"Hostel": 350, "Cafeteria": 260, "Admin Block": 150, "Academic Block": 90, "Library": 0}


campus["Hostel"]["Sports Complex"] = 100
campus["Sports Complex"] = {"Academic Block": 180}
heuristic["Sports Complex"] = 200


def get_h(path):
    return heuristic[path[-1]]


def get_g(path):
    total = 0
    for i in range(len(path) - 1):
        total = total + campus[path[i]][path[i + 1]]
    return total


def gbfs(start, goal):
    frontier = [[start]]
    visited = []

    while len(frontier) > 0:
        frontier.sort(key=get_h)
        path = frontier.pop(0)
        node = path[-1]

        if node in visited:
            continue
        visited.append(    node)

        print("Exploring", node, " path:", path, " h =", get_h(path))

        if node == goal:
            print()
            print("Path found by GBFS:", path)
            print("Total cost of this path:", get_g(path))
            return path

        for neighbour in campus[node]:
            frontier.append(path + [neighbour])

    return None


gbfs("Hostel", "Library")
