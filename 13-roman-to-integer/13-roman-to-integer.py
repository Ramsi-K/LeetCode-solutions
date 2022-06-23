class Solution:
    def romanToInt(self, s: str) -> int:
        ref_dict =  { "I"  :   1,
                     "V"  :   5,
                     "X"  :   10,
                     "L"  :   50,
                     "C"  :   100,
                     "D"  :   500,
                     "M"  :   1000,
                     "F" : 4,
                     "N" : 9,
                     "P" : 40,
                     "O" : 90,
                     "B" : 400,
                     "A" : 900
                    }
        if "IV" in s:
            s = s.replace("IV", "F")
        if "IX" in s:
            s = s.replace("IX", "N")
        if "XL" in s:
            s = s.replace("XL", "P")
        if "XC" in s:
            s = s.replace("XC", "O" )
        if "CD" in s:
            s = s.replace("CD", "B" )
        if "CM" in s:
            s = s.replace("CM", "A")
        
        s = list(s)
        result = 0
        for alphabet in s:
          result += ref_dict[alphabet]
        return result
        