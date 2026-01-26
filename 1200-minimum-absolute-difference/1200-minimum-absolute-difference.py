class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float("inf")
        dic = {}
        ans = []

        for i in range(len(arr)-1):
            curr_diff = arr[i+1]-arr[i]
            min_diff = min(min_diff, curr_diff)
            
            if min_diff == curr_diff:
                if curr_diff not in dic:
                    dic[curr_diff]=[]
                dic[curr_diff].append([arr[i], arr[i+1]])
            
        return dic[min_diff]
