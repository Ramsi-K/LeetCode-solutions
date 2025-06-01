class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Helper function: number of integer solutions to a + b + c = n where a, b, c >= 0
        def count_unbounded_solutions(n):
            if n < 0:
                return 0
            return (n + 2) * (n + 1) // 2  # This is C(n + 2, 2)

        # Inclusion-Exclusion formula:
        total = count_unbounded_solutions(n)
        subtract_1 = 3 * count_unbounded_solutions(n - (limit + 1))
        add_back_2 = 3 * count_unbounded_solutions(n - 2 * (limit + 1))
        subtract_3 = count_unbounded_solutions(n - 3 * (limit + 1))

        return total - subtract_1 + add_back_2 - subtract_3
