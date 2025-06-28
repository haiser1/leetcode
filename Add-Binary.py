class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = int(a, 2) + int(b, 2)
        bin_sum = bin(result)[2:]
        return str(bin_sum)
        