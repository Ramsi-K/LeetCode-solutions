from collections import deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n + 1)]  # 1-based indexing
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [False] * (n + 1)
        total_groups = 0
        
        for node in range(1, n + 1):
            if not visited[node]:
                # Find all nodes in the current component using BFS
                component = []
                queue = deque([node])
                visited[node] = True
                component.append(node)
                while queue:
                    u = queue.popleft()
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            component.append(v)
                            queue.append(v)
                
                # Check if the component is bipartite
                color = [-1] * (n + 1)
                is_bipartite = True
                start = component[0]
                color[start] = 0
                queue = deque([start])
                
                while queue and is_bipartite:
                    u = queue.popleft()
                    for v in adj[u]:
                        if color[v] == -1:
                            color[v] = color[u] ^ 1
                            queue.append(v)
                        elif color[v] == color[u]:
                            is_bipartite = False
                            break
                    if not is_bipartite:
                        break
                
                if not is_bipartite:
                    return -1
                
                # Compute the diameter of the component
                max_distance = 0
                for u in component:
                    distance = [-1] * (n + 1)
                    distance[u] = 0
                    queue = deque([u])
                    while queue:
                        current = queue.popleft()
                        for v in adj[current]:
                            if distance[v] == -1:
                                distance[v] = distance[current] + 1
                                queue.append(v)
                    current_max = max(distance[v] for v in component)
                    if current_max > max_distance:
                        max_distance = current_max
                
                total_groups += (max_distance + 1)
        
        return total_groups