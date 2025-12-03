class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # Group segments by slope
        groups_by_slope = defaultdict(list)
        # Group segments by midpoint (parallelograms detection)
        groups_by_mid = defaultdict(list)

        # Process all point pairs
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y1 - y2
                dx = x1 - x2
                # Calculate slope (handle vertical case)
                slope_val = dy / dx if dx else float('inf')
                # Calculate intercept (handle vertical case)
                intercept_val = (y1 * dx - x1 * dy) / dx if dx else x1
                
                groups_by_slope[slope_val].append(intercept_val)
                groups_by_mid[(x1 + x2, y1 + y2)].append(slope_val)

        ans = 0
        
        # Count all parallel segment pairs (including parallelograms)
        for intercept_list in groups_by_slope.values():
            if len(intercept_list) < 2:
                continue
            curr = 0
            for cnt in Counter(intercept_list).values():
                ans += curr * cnt  # Add pairs with new intercepts
                curr += cnt
        
        # Remove parallelogram duplicates (double-counted)
        for slope_list in groups_by_mid.values():
            if len(slope_list) < 2:
                continue
            curr = 0
            for cnt in Counter(slope_list).values():
                ans -= curr * cnt  # Subtract parallelogram overcount
                curr += cnt

        return ans