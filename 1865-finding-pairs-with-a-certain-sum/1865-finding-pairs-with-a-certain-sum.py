from collections import Counter

class FindSumPairs:
    def __init__(self, nums1, nums2):
        self.n1 = nums1
        self.n2 = nums2

    def add(self, index, val):
        self.n2[index] += val

    def count(self, tot):
        freq = Counter(self.n2)
        res = 0
        for x in self.n1:
            res += freq[tot - x]
        return res
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)