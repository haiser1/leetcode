class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        index = []
        for x in matrix:
            if 0 in x:
                for i in range(len(x)):
                    if x[i] == 0:
                        index.append(i)
                    x[i] = 0
        
        for m in matrix:
            if 0 in m:
                continue
            for i in index:
                m[i] = 0 
                