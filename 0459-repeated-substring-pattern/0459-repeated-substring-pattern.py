class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        factors = [i for i in range(1, n) if n % i == 0]

        for i in factors[::-1]:
            if i == 1:
                subsets = list(s)
                print(subsets)
                return subsets.count(subsets[0]) == n

            else:                    
                chunks, chunk_size = n, n//i
                subsets = [s[j:j+chunk_size] for j in range(0, chunks, chunk_size)]
                if subsets.count(subsets[0]) == i : return True
        
        return False