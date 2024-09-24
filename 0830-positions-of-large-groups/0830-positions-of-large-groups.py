class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        i = 0  # Pointer to track the start of each group

        while i < len(s):
            count = 1  # To count occurrences of the same character
            
            # Check for consecutive identical characters
            while i + count < len(s) and s[i + count] == s[i]:
                count += 1
            
            # If the group is large (3 or more characters), add the start and end indices
            if count >= 3:
                result.append([i, i + count - 1])
            
            # Move the pointer to the next group
            i += count
        
        return result

        # out = []
        # i = 0
        # if len(s) <= 2: return []

        # while i < len(s)-2:
        #     if s[i] == s[i+1] == s[i+2]:
        #         start = i
        #         end = i+2
        #         while end + 1 < len(s) and s[end + 1] == s[i]:
        #             end += 1
        #         out.append([start, end])
        #         i = end + 1
        #     else:
        #         i+=1
        # # print(out)
        # return out







