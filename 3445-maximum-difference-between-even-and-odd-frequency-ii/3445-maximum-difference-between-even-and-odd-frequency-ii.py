class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        @lru_cache(maxsize = 8 * len(s))
        def bestSub(odd, even, isOdd, isEven, index, evenExists):
            if index == len(s):
                if isOdd and isEven and evenExists:
                    return 0
                else:
                    return -math.inf
            if s[index] == odd:
                if isOdd and isEven and evenExists:
                    return max(0, 1 + bestSub(odd, even, not isOdd, isEven, index + 1, evenExists))
                else:
                    return 1 + bestSub(odd, even, not isOdd, isEven, index + 1, evenExists)
            elif s[index] == even:
                if isOdd and isEven and evenExists:
                    return max(0, -1 + bestSub(odd, even, isOdd,  not isEven, index + 1, True))
                else:
                    return -1 + bestSub(odd, even, isOdd, not isEven, index + 1, True)
            else:
                if isOdd and isEven and evenExists:
                    return max(0, bestSub(odd, even, isOdd, isEven, index + 1, evenExists))
                else:
                    return bestSub(odd, even, isOdd, isEven, index + 1, evenExists)
        
        
        nums = ['0', '1', '2', '3', '4']
        combos = []
        for num in nums:
            for num2 in nums:
                if num2 != num:
                    combos.append((num, num2))

        #sliding window
        
        ans = -math.inf
        for odd, even, in combos:
            end = 0
            counter = {}
        
            for start in range(len(s) - k + 1):
                while end < (start + k):
                    char = s[end]
                    counter[char] = counter.get(char, 0) + 1
                    end += 1
                
                #what happens if we start here?
                index = start + k
                oddCount = counter.get(odd, 0)
                evenCount = counter.get(even, 0)
                currCombo = oddCount - evenCount
                currCombo += bestSub(odd, even, oddCount % 2 == 1, evenCount % 2 == 0, index, evenCount > 0)
                ans = max(ans, currCombo)
                # print(currCombo, odd, even, counter, start, end, index)
                counter[s[start]] -= 1
        return ans