class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # Step 1: Sort the words lexicographically
        words.sort()
        
        # Step 2: Iteratively filter the words
        filtered = words
        for i in range(len(pref)):
            # Filter based on the i-th character of the prefix
            filtered = [word for word in filtered if len(word) > i and word[i] == pref[i]]
            # If no words match, we can stop early
            if not filtered:
                break
        
        return len(filtered)
            # count = 0
        # for word in words:
        #     if word.startswith(pref):
        #         count += 1
        # return count