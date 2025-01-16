class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1, xor2 = 0, 0
    
        # Compute XOR of all elements in nums1 and nums2
        for num in nums1:
            xor1 ^= num
        for num in nums2:
            xor2 ^= num
        
        # If nums1's length is odd, each element of nums2 contributes to the result
        # If nums2's length is odd, each element of nums1 contributes to the result
        result = 0
        if len(nums1) % 2 == 1:
            result ^= xor2
        if len(nums2) % 2 == 1:
            result ^= xor1
        
        return result