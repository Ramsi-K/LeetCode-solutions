from typing import List
from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Build the adjacency list for the graph
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)  # a is a prerequisite for b, so edge from a to b
        
        # Initialize the reachability matrix
        reach = [[False] * numCourses for _ in range(numCourses)]
        
        # Precompute reachability for each course using BFS
        for u in range(numCourses):
            queue = deque([u])
            visited = set([u])
            while queue:
                current = queue.popleft()
                for neighbor in adj[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            # Mark all reachable nodes from u
            for v in visited:
                reach[u][v] = True
        
        # Answer each query by checking the reachability matrix
        return [reach[u][v] for u, v in queries]