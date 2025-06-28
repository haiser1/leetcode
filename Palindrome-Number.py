class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        palindrome = int(str(x)[::-1])
        if x == palindrome:
            return True
        else:
            return False
        