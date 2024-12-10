class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        for num in nums1:
            index = nums2.index(num)
            found = next((elem for elem in nums2[index + 1:] if elem > num), -1)
            out.append(found)
        
        # print(out)
        return out
