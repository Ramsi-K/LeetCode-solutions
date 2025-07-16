class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        odds = []
        evens = []
        even_odd = []
        odd_even = []

        for num in nums:
            if num % 2 == 0:
                evens.append(num)
                if len(even_odd) == 0 or even_odd[-1] % 2 == 1:
                    even_odd.append(num)
                if len(odd_even) > 0 and odd_even[-1] % 2 == 1:
                    odd_even.append(num)
            else:
                odds.append(num)
                if len(even_odd) > 0 and even_odd[-1] % 2 == 0:
                    even_odd.append(num)
                if len(odd_even) == 0 or odd_even[-1] % 2 == 0:
                    odd_even.append(num)
        
        return max(len(odds), len(evens), len(even_odd), len(odd_even))
