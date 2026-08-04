
def DFS(graph, vertex, visited):
    visited.add(vertex) # Mark the current vertex as visited
    print(f"Visited: {vertex}")

    # Check every neighbour of the current vertex
    for neighbour in graph[vertex]:
        print(f"Checking neighbour '{neighbour}' of '{vertex}'")
        if neighbour not in visited: # Visit the neighbour only if it has not been visited yet
            print(f"'{neighbour}' has not been visited. Going deeper...\n")
            DFS(graph, neighbour, visited)
        else:
            print(f"'{neighbour}' was already visited. Skipping.\n")
            
            

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

visited = set()

print("Starting DFS from A...\n")
DFS(graph, "A", visited)

print("\nTraversal complete!")
print("Visited nodes:", visited)

