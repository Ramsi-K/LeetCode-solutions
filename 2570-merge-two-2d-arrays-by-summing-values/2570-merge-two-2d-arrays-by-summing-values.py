class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        
        while i < n and j < m:
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            
            if id1 < id2:
                result.append([id1, val1])
                i += 1
            elif id1 > id2:
                result.append([id2, val2])
                j += 1
            else:
                result.append([id1, val1 + val2])
                i += 1
                j += 1
        
        # Add remaining elements from nums1
        while i < n:
            result.append(nums1[i])
            i += 1
        
        # Add remaining elements from nums2
        while j < m:
            result.append(nums2[j])
            j += 1
        
        return result