class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def compute_best(graph, size, depth_lim):
            if depth_lim < 0:
                return 0
            seen = [0]*size
            stamp = 1
            best = 0
            for s in range(size):
                cnt = 1
                seen[s] = stamp
                q = deque([s])
                d = 0
                while q and d < depth_lim:
                    for _ in range(len(q)):
                        u = q.popleft()
                        for w in graph[u]:
                            if seen[w] != stamp:
                                seen[w] = stamp
                                q.append(w)
                                cnt += 1
                    d += 1
                best = max(best, cnt)
                stamp += 1
            return best


        # Adjacency for both trees
        n, m = len(edges1) + 1, len(edges2) + 1
        g1 = [[] for _ in range(n)]
        for u,v in edges1:
            g1[u].append(v)
            g1[v].append(u)

        g2 = [[] for _ in range(m)]
        for u,v in edges2:
            g2[u].append(v)
            g2[v].append(u)

        # Second tree: dist₂ ≤ k–1
        best2 = compute_best(g2, m, k-1)

        # First tree: dist₁ ≤ k
        res, seen, stamp = [0]*n, [0]*n, 1
        for s in range(n):
            cnt, d = 1, 0
            seen[s] = stamp
            q = deque([s])
            while q and d < k:
                for _ in range(len(q)):
                    u = q.popleft()
                    for w in g1[u]:
                        if seen[w] != stamp:
                            seen[w] = stamp
                            q.append(w)
                            cnt += 1
                d += 1
            res[s] = cnt + best2
            stamp += 1

        return res