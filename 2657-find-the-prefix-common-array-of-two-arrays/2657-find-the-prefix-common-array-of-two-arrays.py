class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen_a = set()
        seen_b = set()
        common_count = 0
        result = []

        for i in range(n):
            # Add current elements to the respective sets
            seen_a.add(A[i])
            seen_b.add(B[i])

            # If A[i] is in B's seen set, it's a new common element
            if A[i] in seen_b:
                common_count += 1

            # If B[i] is in A's seen set, it's a new common element
            if B[i] in seen_a:
                common_count += 1

            # Handle the case where A[i] == B[i] (avoid double counting)
            if A[i] == B[i]:
                common_count -= 1

            # Append the current common count to the result
            result.append(common_count)

        return result