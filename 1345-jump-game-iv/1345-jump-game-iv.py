class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = defaultdict(list)
        for i, x in enumerate(arr):
            d[x].append(i)

        n = len(arr)
        visited = [False] * n
        visited[0] = True
        queue = deque([(0, 0)])

        while queue:
            i, val = queue.popleft()
            if i == n - 1:
                return val
            val += 1

            for r in d[arr[i]]:
                if not visited[r]:
                    visited[r] = True
                    queue.append((r, val))
            
            d[arr[i]].clear()

            for di in (i - 1, i + 1):
                if 0 <= di < n and not visited[di]:
                    visited[di] = True
                    queue.append((di, val))