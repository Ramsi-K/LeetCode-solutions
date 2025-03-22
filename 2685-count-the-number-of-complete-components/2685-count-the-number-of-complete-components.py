class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                queue = deque([i])
                visited[i] = True
                nodes = []
                edge_count = 0

                while queue:
                    node = queue.popleft()
                    nodes.append(node)
                    edge_count += len(graph[node])
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)

                size = len(nodes)
                if edge_count == size * (size - 1):
                    count += 1

        return count