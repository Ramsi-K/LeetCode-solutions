class Solution:
    def minimumLength(self, s: str) -> int:
        # Step 1: Build a dictionary to count occurrences
        char_count = defaultdict(int)
        for char in s:
            char_count[char] += 1

        # Step 2: Remove triplets mathematically
        removable = 0
        for count in char_count.values():
            if count >= 3:
                # Calculate removable indices based on triplets
                triplets = (count - 1) // 2
                removable += triplets * 2

        # Step 3: Return the remaining string length
        return len(s) - removable