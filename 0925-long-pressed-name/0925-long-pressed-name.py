class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def group_chars(s):
            return [(char, len(list(group))) for char, group in itertools.groupby(s)]
    
        grouped_name = group_chars(name)
        grouped_typed = group_chars(typed)
        
        if len(grouped_name) != len(grouped_typed):
            return False
        
        for (char_n, count_n), (char_t, count_t) in zip(grouped_name, grouped_typed):
            if char_n != char_t or count_n > count_t:
                return False
        
        return True

        
        # if name == typed : return True
        # if len(name) >= len(typed) : return False
        # # if set(name) != set(typed) : return False
        
        # i, j = 0, 0  
        
        # while j < len(typed):
        #     if i < len(name) and name[i] == typed[j]:
        #         i += 1
        #         j += 1
        #     elif j > 0 and typed[j] == typed[j - 1]:
        #         j += 1
        #     else:
        #         return False
        
        # return i == len(name)