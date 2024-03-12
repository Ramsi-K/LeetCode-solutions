class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_len = len(nums)
        nums.sort()
        threesum_list = []
        
        if num_len<3:
            return []
        
        for i, val1 in enumerate(nums):
            if i>0 and val1 == nums[i-1]:
                continue
            
            l, r = i+1, num_len - 1
            
            while l < r:
                threesum = val1 + nums[l] + nums[r]
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -=1
                else:
                   threesum_list.append([val1, nums[l], nums[r]]) 
                   l += 1
                   while nums[l] == nums[l-1] and l < r:
                       l +=1
        return threesum_list