class Solution:
    def isPalindrome(self, x: int) -> bool:
        return "".join(list(reversed(str(x)))) == str(x)