class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # n = len(s)
        # factors = [i for i in range(1, n) if n % i == 0]

        # for i in factors[::-1]:
        #     if i == 1:
        #         subsets = list(s)
        #         # print(subsets)
        #     else:                    
        #         chunks, chunk_size = n, n//i
        #         subsets = [s[j:j+chunk_size] for j in range(0, chunks, chunk_size)]
            
        #     counts = {subsets[i]: subsets.count(subsets[i]) for i in range(len(subsets))}
        #     # print(subsets)
        #     # print(counts)
        #     # print(len(counts))

        #     if len(counts) == 1: return True
        
        # return False

        if not s:
            return False   
        ss = (s + s)[1:-1]
        return ss.find(s) != -1