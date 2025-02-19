class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Find the kth lexicographically sorted happy string of length n
        
        Args:
            n: The length of the happy string
            k: The position in lexicographical order to return
            
        Returns:
            The kth happy string or an empty string if k exceeds the count
        """
        chars = ['a', 'b', 'c']
        
        def generateHappyStrings(length, last_char, current_string):
            """Recursively generate all happy strings"""
            # Base case: we've built a string of the target length
            if length == 0:
                return [current_string]
            
            results = []
            
            # Try adding each character
            for char in chars:
                # Skip if this would create adjacent identical characters
                if char == last_char:
                    continue
                    
                # Recursive call to build the rest of the string
                new_strings = generateHappyStrings(
                    length - 1,
                    char,
                    current_string + char
                )
                
                results.extend(new_strings)
                
            return results
        
        # Generate all happy strings of length n (with no previous character constraint)
        happy_strings = generateHappyStrings(n, '', '')
        
        # Return the kth string or empty string if k is too large
        return happy_strings[k-1] if k <= len(happy_strings) else ""