from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n  # -1 indicates uncolored, 0 and 1 are the two colors
        
        for node in range(n):
            if colors[node] == -1:
                # Start BFS to color this component
                colors[node] = 0
                queue = deque([node])
                
                while queue:
                    current = queue.popleft()
                    for neighbor in graph[current]:
                        if colors[neighbor] == -1:
                            colors[neighbor] = colors[current] ^ 1  # Toggle color
                            queue.append(neighbor)
                        elif colors[neighbor] == colors[current]:
                            return False  # Found conflict, not bipartite
        return True