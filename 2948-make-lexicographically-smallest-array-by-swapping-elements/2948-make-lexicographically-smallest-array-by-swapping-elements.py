class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        from collections import defaultdict
        
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [1] * size

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)
                if root_x != root_y:
                    if self.rank[root_x] > self.rank[root_y]:
                        self.parent[root_y] = root_x
                    elif self.rank[root_x] < self.rank[root_y]:
                        self.parent[root_x] = root_y
                    else:
                        self.parent[root_y] = root_x
                        self.rank[root_x] += 1

        n = len(nums)
        uf = UnionFind(n)
        
        # Sort the array based on the values
        sorted_indices = sorted(range(n), key=lambda x: nums[x])
        
        # Union adjacent indices in the sorted array if their difference <= limit
        for i in range(n - 1):
            if abs(nums[sorted_indices[i]] - nums[sorted_indices[i + 1]]) <= limit:
                uf.union(sorted_indices[i], sorted_indices[i + 1])
        
        # Group indices by their connected components
        groups = defaultdict(list)
        for i in range(n):
            groups[uf.find(i)].append(i)
        
        # Sort values within each group and place them back in the array
        result = nums[:]
        for group in groups.values():
            values = sorted(result[i] for i in group)
            for idx, val in zip(sorted(group), values):
                result[idx] = val

        return result
