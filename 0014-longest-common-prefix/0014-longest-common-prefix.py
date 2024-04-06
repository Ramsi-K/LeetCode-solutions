class Solution:        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def check_string(i, string_list):
            
            output = [j for j in string_list if j.startswith(i)] 
            
            if len(i) == 1 :
                return "" if len(output)!=len(string_list) else i            
            if len(output) == len(string_list):
                return i             
            else:
                return check_string(i[:-1],string_list)
        
        if strs[1:]:
            return check_string(i=strs[0], string_list=strs[1:])
        else:
            return strs[0]