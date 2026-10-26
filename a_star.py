import heapq

def astar(graph, start, goal, heuristic):
    node_list = [(heuristic[start], 0, start, [start])]  # (f, g, node, path)
    visited = set()

    while node_list:
        fn, gn, current_node, path = heapq.heappop(node_list)

        if current_node == goal:
            return path, gn  # path and total cost

        if current_node in visited:
            continue
        visited.add(current_node)

        for child_node, edge in graph[current_node]:
            if child_node not in visited:
                g_new = gn + edge
                f_new = g_new + heuristic[child_node]
                heapq.heappush(node_list, (f_new, g_new, child_node, path + [child_node]))

    return None, None


g = {
    "Dhaka": [("Gazipur", 10), ("Tangail", 15), ("Cumilla", 20)],
    "Gazipur": [("Dhaka", 10), ("Mymensingh", 12)],
    "Mymensingh": [("Gazipur", 12), ("Bogura", 8)],
    "Bogura": [("Mymensingh", 8), ("Natore", 5), ("Rajshahi", 7), ("Tangail", 6)],
    "Tangail": [("Dhaka", 15), ("Bogura", 6)],
    "Cumilla": [("Dhaka", 20), ("Chittagong", 18)],
    "Chittagong": [("Cumilla", 18), ("Barishal", 10)],
    "Natore": [("Bogura", 5)],
    "Rajshahi": [("Bogura", 7)],
    "Barishal": [("Chittagong", 10)]
}

heu={
    "Dhaka": 300,
    "Gazipur": 254,
    "Mymensingh": 400,
    "Bogura": 550,
    "Tangail": 460,
    "Cumilla": 600,
    "Chittagong": 780,
    "Natore": 420,
    "Rajshahi": 650,
    "Barishal": 800
}

path, cost = astar(g, 'Dhaka', 'Barishal', heu)
print("Final Path:", path)
print("Total Cost:", cost)