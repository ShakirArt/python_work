from collections import deque
def bfs(graph, start):
   visited = set() 
   queue = deque([start]) 
   visited.add(start)
   while queue:
       value = queue.popleft() 
       print(value, end=" ") # Process the vertex
       for i in graph[value]:
           if i not in visited:
               visited.add(i)
               queue.append(i)
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

bfs(graph, "Dhaka")