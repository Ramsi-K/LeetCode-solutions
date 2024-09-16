class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {item1: (i + j) for i, item1 in enumerate(list1) for j, item2 in enumerate(list2) if item1 == item2}
        res = [k for k, v in d.items() if v == min(d.values())]
        return res