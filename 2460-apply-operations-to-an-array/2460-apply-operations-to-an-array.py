class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
        # Perform the operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Shift all zeros to the end
        write_pointer = 0
        for read_pointer in range(n):
            if nums[read_pointer] != 0:
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1
        
        # Fill the remaining positions with zeros
        while write_pointer < n:
            nums[write_pointer] = 0
            write_pointer += 1
        
        return nums