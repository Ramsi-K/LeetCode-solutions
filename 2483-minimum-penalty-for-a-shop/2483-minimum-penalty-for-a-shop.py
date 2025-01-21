class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_gain = 0  # Maximum gain (minimized penalty so far)
        current_gain = 0  # Running net gain
        best_closing_hour = -1  # Earliest hour with the maximum gain

        # Iterate through each hour and update the gain
        for hour, customer in enumerate(customers):
            if customer == 'Y':  # Gain for a customer visiting
                current_gain += 1
            else:  # Penalty for no customer
                current_gain -= 1

            # Update the best hour if the current gain exceeds max gain
            if current_gain > max_gain:
                max_gain = current_gain
                best_closing_hour = hour

        # Return the hour immediately after the hour with the maximum gain
        return best_closing_hour + 1