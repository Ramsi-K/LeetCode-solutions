class Solution:
    def minimumLength(self, s: str) -> int:
        # Step 1: Build a dictionary mapping characters to their indices
        char_indices = defaultdict(list)
        for i, char in enumerate(s):
            char_indices[char].append(i)

        # Step 2: Process characters with sufficient occurrences mathematically
        removed_count = 0
        for indices in char_indices.values():
            if len(indices) >= 3:
                # Calculate the number of removable triplets
                triplets = (len(indices) - 1) // 2
                removed_count += triplets * 2

        # Step 3: Return the remaining string length
        return len(s) - removed_count