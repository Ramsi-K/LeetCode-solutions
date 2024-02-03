class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        # print(l, r)
        # print(len(height))
        
        if len(height) == 2:
            res = min(height[l], height[r])
        
        while l < r:
            area = (r-l) * min(height[l], height[r])
            # print(area)
            res = max(res, area)
            
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        # print(res)
        return res
        