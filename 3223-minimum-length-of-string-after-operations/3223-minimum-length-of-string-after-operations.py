class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        char_indices = defaultdict(list)

        # Step 1: Build a dictionary mapping characters to their indices
        for i, char in enumerate(s):
            char_indices[char].append(i)

        # Step 2: Count and remove triplets mathematically
        removed_count = 0
        for indices in char_indices.values():
            # Calculate the number of triplets that can be removed
            while len(indices) >= 3:
                removed_count += 2  # Remove leftmost and rightmost indices
                indices.pop(0)  # Remove the leftmost index
                indices.pop(-1)  # Remove the rightmost index

        # Step 3: Return the remaining length
        return n - removed_count