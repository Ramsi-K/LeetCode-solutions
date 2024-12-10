class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    for elem in nums2[j+1:]:
                        if elem > nums2[j]:
                            out.append(elem)
                            break
                    else:
                        out.append(-1)
        
        # print(out)
        return out
