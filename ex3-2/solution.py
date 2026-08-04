def graph_cycle_detector(graph: dict[int, list[int]]) -> bool:
    visited = set()     # fully explored, known cycle-free
    in_path = set()     # nodes on the current DFS path

    def dfs(node: int) -> bool:
        if node in in_path:     # back-edge: we walked into our own path
            return True
        if node in visited:
            return False

        visited.add(node)
        in_path.add(node)

        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True

        in_path.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False
