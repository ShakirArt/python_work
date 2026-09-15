def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for i in graph[start]:
        if i not in visited:
            dfs(graph, i, visited)

graph = {
    "Dhaka": ["Gazipur", "Tangail", "Cumilla"],
    "Gazipur": ["Dhaka", "Mymensingh"],
    "Mymensingh": ["Gazipur", "Bogura"],
    "Bogura": ["Mymensingh", "Natore", "Rajshahi", "Tangail"],
    "Tangail": ["Dhaka", "Bogura"],
    "Cumilla": ["Dhaka", "Chittagong"],
    "Chittagong": ["Cumilla", "Barishal"],
    "Natore": [],
    "Rajshahi": [],
    "Barishal": []
}

dfs(graph, "Dhaka")
