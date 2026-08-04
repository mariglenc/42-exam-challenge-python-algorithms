# def graph_cycle_detector(graph: list) -> bool:
#     if not graph:
#         return False

#     visited = set()
#     in_path = set()

#     def dfs(node: int):
#         if node in in_path:
#             return True

#         if node in visited:
#             return False

#         visited.add(node)
#         in_path.add(node)

#         for neighbor in graph.get(node, []):
#             if neighbor in in_path:
#                 return True
#             if neighbor not in visited:
#                 if dfs(neighbor):
#                     return True

#         in_path.remove(node)
#         return False

#     for node in graph:
#         if node not in visited:
#             if dfs(node):
#                 return True

#     return False


def graph_cycle_detector(graph: dict[int, list[int]]) -> bool:
    visited = set()
    in_path = set()

    def dfs(node: int):
        # Base cases handle the state checks automatically
        if node in in_path:
            return True
        if node in visited:
            return False

        visited.add(node)
        in_path.add(node)

        # Let the recursion handle the logic checks
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