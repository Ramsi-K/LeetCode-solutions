class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        n = len(s)
        chunks, chunk_size = n, k
        subsets = [s[j: j + chunk_size] for j in range(chunks - chunk_size, -1, -chunk_size)][::-1]
        # print(subsets)
        if n % k: 
            # print("HERE BE YOUR MISSING VALUES")
            subsets.insert(0, s[: n%k])
        # print(subsets)
        # print("-".join(subsets))
        return "-".join(subsets)