class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt, res = Counter(words), 0
        for w, c in cnt.items(): # Address non-palindromic pairs
            rev = w[::-1]
            if w < rev and rev in cnt:
                res += 4 * min(c, cnt[rev])

        for w, c in cnt.items(): # Address palindromic words in pairs
            if w[0] == w[1]:     # palindromic word like 'aa'
                res += 4 * (c // 2)

        # Check and potentially add one palindromic word in center
        if any(w[0] == w[1] and cnt[w] % 2 for w in cnt):
            res += 2
            
        return res