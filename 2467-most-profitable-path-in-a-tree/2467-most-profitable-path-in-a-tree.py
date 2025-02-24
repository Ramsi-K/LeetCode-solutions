class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Find Bob's path and the time he reaches each node
        def find_bob_path_and_time():
            parent = {}
            visited = set()
            queue = deque([bob])
            while queue:
                node = queue.popleft()
                if node == 0:
                    break
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        parent[neighbor] = node
                        queue.append(neighbor)
            path = []
            current = 0
            while current != bob:
                path.append(current)
                current = parent[current]
            path.append(bob)
            path = path[::-1]
            # Calculate the time Bob reaches each node
            time = {node: i for i, node in enumerate(path)}
            return time
        
        bob_time = find_bob_path_and_time()
        
        # DFS to find Alice's paths and calculate income
        max_income = -float('inf')
        
        def dfs(node, parent, time, income):
            nonlocal max_income
            # Update income based on Bob's visit time
            if node in bob_time:
                if bob_time[node] == time:
                    # Both reach at the same time
                    income += amount[node] // 2
                elif bob_time[node] > time:
                    # Bob hasn't reached yet, Alice takes full amount
                    income += amount[node]
            else:
                # Bob never reaches this node, Alice takes full amount
                income += amount[node]
            
            # If it's a leaf node, update max_income
            if len(adj[node]) == 1 and node != 0:
                max_income = max(max_income, income)
                return
            
            # Continue DFS
            for neighbor in adj[node]:
                if neighbor != parent:
                    dfs(neighbor, node, time + 1, income)
        
        dfs(0, -1, 0, 0)
        return max_income