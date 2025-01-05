class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        delta = [0] * (n + 1)  # Extra space to handle end boundary

        # Step 1: Apply shifts directly to delta array
        for start, end, direction in shifts:
            shift_value = 1 if direction == 1 else -1
            delta[start] += shift_value
            if end + 1 < n:
                delta[end + 1] -= shift_value

        # Step 2: Compute cumulative shifts
        cumulative_shift = 0
        result = []

        for i in range(n):
            cumulative_shift += delta[i]
            # Step 3: Apply shift to the character with wraparound
            new_char = chr((ord(s[i]) - ord('a') + cumulative_shift) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)