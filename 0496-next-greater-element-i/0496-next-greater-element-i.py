class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        
        for element in nums1:
            ind = nums2.index(element)
            # print(ind)
            for i in range(ind, len(nums2)):
                if nums2[i] > element:
                    stack.append(nums2[i])
                    break
            else:
                stack.append(-1)
        
        # print(stack)
        return stack
