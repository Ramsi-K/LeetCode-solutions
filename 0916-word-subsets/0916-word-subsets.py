class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Step 1: Combine the maximum frequency requirements from words2
        max_b_count = [0] * 26  # Array to hold max counts for each letter

        for b in words2:
            b_count = [0] * 26
            for char in b:
                idx = ord(char) - ord('a')
                b_count[idx] += 1
                max_b_count[idx] = max(max_b_count[idx], b_count[idx])

        # Step 2: Filter words1 based on the combined requirements
        result = []
        for a in words1:
            a_count = [0] * 26
            for char in a:
                idx = ord(char) - ord('a')
                a_count[idx] += 1

            # Check if word 'a' meets all the requirements
            for idx in range(26):
                if a_count[idx] < max_b_count[idx]:
                    break  # Doesn't meet the requirement
            else:
                result.append(a)  # Meets all requirements

        return result