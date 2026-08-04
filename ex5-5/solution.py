def graph_cycle_detector(graph: dict[int, list[int]]) -> bool:
    visited = set()
    in_path = set()

    def dfs(node: int) -> bool:
        if node in in_path:      # back-edge: node is on the current path
            return True
        if node in visited:      # fully explored earlier, no cycle through it
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


if __name__ == "__main__":
    print(graph_cycle_detector({0: [1], 1: [2], 2: [0]}))  # True
    print(graph_cycle_detector({0: [1], 1: [2], 2: []}))   # False
    print(graph_cycle_detector({}))                        # False
