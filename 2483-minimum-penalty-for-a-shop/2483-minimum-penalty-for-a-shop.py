class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        
        # Convert 'Y' -> 1 and 'N' -> 0
        customer_values = [1 if c == 'Y' else 0 for c in customers]

        # Compute suffix sum (penalty_closed)
        penalty_closed = list(accumulate(customer_values[::-1]))[::-1]

        # Simulate the process
        penalty_open = 0
        min_penalty = float('inf')
        best_hour = 0

        for j in range(n + 1):
            total_penalty = penalty_open + (penalty_closed[j] if j < n else 0)
            if total_penalty < min_penalty:
                min_penalty = total_penalty
                best_hour = j
            
            # Update penalty_open for the next hour
            if j < n and customers[j] == 'N':
                penalty_open += 1

        return best_hour