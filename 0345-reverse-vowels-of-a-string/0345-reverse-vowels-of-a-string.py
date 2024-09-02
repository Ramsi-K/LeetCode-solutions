class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        pointer_1 = 0
        pointer_2 = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        while pointer_1 < pointer_2:
            if s[pointer_1] in vowels and s[pointer_2] in vowels:
                # print(f"S: {s} \nS-poin1: {s[pointer_1]} \nS-point2: {s[pointer_2]}")
                # print(f"Swapping: {s[pointer_1], s[pointer_2]}")
                s[pointer_1], s[pointer_2] = s[pointer_2], s[pointer_1]
                pointer_1 += 1
                pointer_2 -= 1

            elif s[pointer_1] in vowels and s[pointer_2] not in vowels:
                pointer_2 -= 1

            elif s[pointer_1] not in vowels and s[pointer_2] in vowels:
                pointer_1 += 1

            else:
                pointer_1 += 1
                pointer_2 -= 1
        
        return "".join(s)