class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
        # for i in range(n):
        #     if n == 2**i:
        #         return True
        #     if 2**i > n:
        #         return False
        
        # return False