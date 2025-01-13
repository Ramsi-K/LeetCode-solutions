class Solution:
    def minimumLength(self, s: str) -> int:
        # Step 1: Count occurrences of each character
        char_count = Counter(s)

        # Step 2: Compute total removable indices
        removable = sum((count // 3) * 2 for count in char_count.values())

        # Step 3: Return remaining length
        return len(s) - removable