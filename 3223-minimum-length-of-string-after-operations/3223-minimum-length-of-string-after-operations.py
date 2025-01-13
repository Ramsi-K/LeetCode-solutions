class Solution:
    def minimumLength(self, s: str) -> int:
        # Step 1: Build a dictionary mapping characters to their indices
        char_indices = {}
        for i, char in enumerate(s):
            if char not in char_indices:
                char_indices[char] = []
            char_indices[char].append(i)

        # Step 2: Simulate the process of removing triplets
        removed_indices = set()
        while True:
            triplets_removed = False

            # Process each character with at least 3 occurrences
            for char, indices in list(char_indices.items()):
                if len(indices) < 3:
                    continue  # Skip characters with fewer than 3 occurrences

                # Try removing a triplet
                for i in range(1, len(indices) - 1):
                    if indices[i - 1] not in removed_indices and indices[i + 1] not in removed_indices:
                        # Remove the leftmost and rightmost indices around the current one
                        removed_indices.add(indices[i - 1])
                        removed_indices.add(indices[i + 1])
                        triplets_removed = True
                        indices.pop(i + 1)
                        indices.pop(i - 1)
                        break

            if not triplets_removed:
                break  # No more triplets can be removed

        # Step 3: Return the remaining string length
        return len(s) - len(removed_indices)