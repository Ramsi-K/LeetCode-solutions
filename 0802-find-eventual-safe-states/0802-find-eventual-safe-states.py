class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n  # 0 = unvisited, 1 = visiting, 2 = safe

        def dfs(node):
            if state[node] != 0:  # If the node is already processed
                return state[node] == 2  # Return True if the node is safe

            state[node] = 1  # Mark the node as visiting
            for neighbor in graph[node]:
                if not dfs(neighbor):  # If a neighbor is unsafe or part of a cycle
                    return False

            state[node] = 2  # Mark the node as safe
            return True

        # Run DFS for every node
        return [i for i in range(n) if dfs(i)]