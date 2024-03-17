class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() 
        closestSum = inf 
        n = len(nums)
        
        for i in range(n - 2): 
            left, right = i + 1, n - 1
            while left < right:  
                currSum = nums[i] + nums[left] + nums[right]
                if abs(currSum - target) < abs(closestSum - target): 
                    closestSum = currSum
                if currSum < target: 
                    left += 1
                elif currSum > target:
                    right -= 1
                else:
                    return currSum
        
        return closestSum  # Step 7
