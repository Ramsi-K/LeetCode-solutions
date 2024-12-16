class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = Counter(s)

        used = set()
        stack = []
        
        for ch in s:
            freq[ch] -= 1
            
            if ch in used:
                continue
            
            # Ensure lexicographical order by popping characters from the stack
            while stack and stack[-1] > ch and freq[stack[-1]] > 0:
                used.remove(stack.pop())

            stack.append(ch)
            used.add(ch)

        return ''.join(stack)