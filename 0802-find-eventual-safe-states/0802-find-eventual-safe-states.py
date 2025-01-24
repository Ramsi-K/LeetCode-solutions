class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        # Step 1: Reverse the graph
        reverse_graph = defaultdict(list)
        in_degree = [0] * n  # Count of outgoing edges for each node
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reverse_graph[neighbor].append(node)  # Reverse the direction of the edge
            in_degree[node] = len(neighbors)  # Outgoing edges in the original graph

        # Step 2: Identify terminal nodes (nodes with no outgoing edges in the original graph)
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:  # Terminal node
                queue.append(i)

        # Step 3: Perform BFS/Topological Sort to find safe nodes
        safe = [False] * n  # Safe nodes tracker
        while queue:
            node = queue.popleft()
            safe[node] = True  # Mark this node as safe
            for neighbor in reverse_graph[node]:
                in_degree[neighbor] -= 1  # Reduce the outgoing edge count
                if in_degree[neighbor] == 0:  # If no outgoing edges remain, it's safe
                    queue.append(neighbor)

        # Step 4: Collect all safe nodes in sorted order
        return [i for i in range(n) if safe[i]]