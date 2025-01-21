class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        
        # Step 1: Precompute penalties for closed hours (suffix sum for 'Y')
        penalty_closed = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            penalty_closed[i] = penalty_closed[i + 1] + (1 if customers[i] == 'Y' else 0)

        # Step 2: Iterate and calculate penalties dynamically
        penalty_open = 0  # Tracks penalties for open hours (prefix sum for 'N')
        min_penalty = float('inf')
        best_hour = 0

        for j in range(n + 1):
            total_penalty = penalty_open + penalty_closed[j]
            if total_penalty < min_penalty:
                min_penalty = total_penalty
                best_hour = j
            
            # Update penalty_open for the next hour
            if j < n and customers[j] == 'N':
                penalty_open += 1

        return best_hour