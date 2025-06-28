class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result_dividen = dividend / divisor

        result = int(result_dividen)

        min_int32, max_int32 = -2**31, 2**31 - 1

        if result < min_int32:
            return min_int32
        elif result > max_int32:
            return max_int32
        
        return result