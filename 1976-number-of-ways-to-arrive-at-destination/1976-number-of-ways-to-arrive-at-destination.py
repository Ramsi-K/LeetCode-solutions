class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        heap = [(0, 0)]  # (time, node)

        while heap:
            time, u = heapq.heappop(heap)
            if time > dist[u]:
                continue
            for v, t in graph[u]:
                if time + t < dist[v]:
                    dist[v] = time + t
                    ways[v] = ways[u]
                    heapq.heappush(heap, (dist[v], v))
                elif time + t == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1]