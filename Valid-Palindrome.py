class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabets = ''.join(re.findall(r'[a-zA-Z0-9]', s)).lower()[::-1]

        return alphabets == alphabets[::-1]