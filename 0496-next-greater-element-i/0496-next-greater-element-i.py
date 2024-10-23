class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        # Process nums2 to find the next greater element for each element
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        # For elements that do not have a next greater element, mark them as -1
        while stack:
            next_greater[stack.pop()] = -1

        # Now, for each element in nums1, simply look up the next greater element
        return [next_greater[num] for num in nums1]

        # stack = []
        
        # for element in nums1:
        #     ind = nums2.index(element)
        #     # print(ind)
        #     for i in range(ind, len(nums2)):
        #         if nums2[i] > element:
        #             stack.append(nums2[i])
        #             break
        #     else:
        #         stack.append(-1)
        
        # # print(stack)
        # return stack
