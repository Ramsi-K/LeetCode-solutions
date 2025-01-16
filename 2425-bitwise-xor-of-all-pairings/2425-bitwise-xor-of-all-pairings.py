class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Get the lengths of nums1 and nums2
        len_nums1, len_nums2 = len(nums1), len(nums2)
        
        # Initialize the XOR result
        xor_result = 0
        
        # If nums2 has an odd length, each element of nums1 contributes to the XOR
        if len_nums2 % 2 == 1:
            for num in nums1:
                xor_result ^= num  # Add each element of nums1 to the XOR result
        
        # If nums1 has an odd length, each element of nums2 contributes to the XOR
        if len_nums1 % 2 == 1:
            for num in nums2:
                xor_result ^= num  # Add each element of nums2 to the XOR result
        
        # Return the final XOR result
        return xor_result