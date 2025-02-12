class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(n: int) -> int:
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total

        # Dictionary to group numbers by their digit sum.
        groups = defaultdict(list)
        
        # Group the numbers by their digit sum.
        for num in nums:
            s = digit_sum(num)
            groups[s].append(num)
        
        max_sum = -1
        # For each group, if there are at least two numbers, update max_sum.
        for s, numbers in groups.items():
            if len(numbers) >= 2:
                # Sort the group to easily get the two largest numbers.
                numbers.sort()
                candidate = numbers[-1] + numbers[-2]
                max_sum = max(max_sum, candidate)
        
        return max_sum