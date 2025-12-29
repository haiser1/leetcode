class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        for i in grid:
            for j in i:
                if j < 0:
                    result += 1
        
        return result
