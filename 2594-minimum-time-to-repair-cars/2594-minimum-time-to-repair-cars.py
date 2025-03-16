class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair_in_time(t):
            """Checks if we can repair all cars in at most `t` minutes."""
            total_cars = 0
            for r in ranks:
                max_cars = int((t // r) ** 0.5)  # Solve n^2 <= t/r -> n <= sqrt(t/r)
                total_cars += max_cars
                if total_cars >= cars:  # Early exit if already possible
                    return True
            return False

        # Binary search on minimum time required
        low, high = 1, min(ranks) * cars * cars
        best_time = high

        while low <= high:
            mid = (low + high) // 2
            if can_repair_in_time(mid):
                best_time = mid  # Store possible answer
                high = mid - 1   # Try for a smaller time
            else:
                low = mid + 1    # Increase time

        return best_time