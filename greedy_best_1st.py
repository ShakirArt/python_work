import heapq

def gbfs(graph, start, goal, heuristic):
    node_list = [(heuristic[start], start, [start])]
    visited = set()

    while node_list:
        hn, current_node, path = heapq.heappop(node_list)

        if current_node == goal:
            return path  # stop as soon as goal is reached

        if current_node in visited:
            continue
        visited.add(current_node)

        for child_node, edge in graph[current_node]:
            if child_node not in visited:
                heapq.heappush(node_list, (heuristic[child_node], child_node, path + [child_node]))

    return None




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


path = gbfs(g, 'Dhaka', 'Barishal', heu)
print("Final Path:", path)


