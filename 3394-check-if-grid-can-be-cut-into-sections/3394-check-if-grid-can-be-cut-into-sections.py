class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check(axis):
            if axis == 'x':
                intervals = [(x1, x2) for x1, _, x2, _ in rectangles]
            else:
                intervals = [(y1, y2) for _, y1, _, y2 in rectangles]

            intervals.sort()
            splits = []

            max_end = intervals[0][1]
            for i in range(1, len(intervals)):
                start, end = intervals[i]
                if start >= max_end:
                    splits.append(i)
                    if len(splits) >= 2:
                        return True
                max_end = max(max_end, end)
            return False

        return check('x') or check('y')