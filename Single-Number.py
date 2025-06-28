class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # [4,1,2,1,2]
        result = 0 # 0 xor 4 = 4, 4 xor 1 = 5, 5 xor 2 = 7, 7 xor 1 = 6, 6 xor 2 = 4

        for num in nums:
            result ^= num
        
        return result
        