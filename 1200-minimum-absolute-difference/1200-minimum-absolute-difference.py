class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float("inf")
        res = []

        for i in range(len(arr) - 1):
            curr_diff = arr[i+1] - arr[i]
            
            if curr_diff < min_diff:
                # Found a new strictly smaller difference: 
                # Reset the list and update min_diff
                min_diff = curr_diff
                res = [[arr[i], arr[i+1]]]
                
            elif curr_diff == min_diff:
                # Found another pair with the same minimum difference
                res.append([arr[i], arr[i+1]])
                
        return res
