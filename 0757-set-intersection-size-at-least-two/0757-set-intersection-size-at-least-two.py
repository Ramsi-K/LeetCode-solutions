class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        res = []
        
        p1 = p2 = -1  # last two placed points
        
        for l, r in intervals:
            count = (p1 >= l) + (p2 >= l)
            
            if count == 2:
                continue
            elif count == 1:
                # add r
                res.append(r)
                p1, p2 = p2, r
            else:
                # add r-1 and r
                res.append(r-1)
                res.append(r)
                p1, p2 = r-1, r
        
        return len(res)
