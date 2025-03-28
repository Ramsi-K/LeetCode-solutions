class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        min_heap = []
        heappush(min_heap, (grid[0][0], 0, 0))
        visited[0][0] = True

        query_with_index = sorted((q, i) for i, q in enumerate(queries))
        answer = [0] * len(queries)
        count = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        for q_val, idx in query_with_index:
            while min_heap and min_heap[0][0] < q_val:
                val, x, y = heappop(min_heap)
                count += 1
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        heappush(min_heap, (grid[nx][ny], nx, ny))
            answer[idx] = count

        return answer