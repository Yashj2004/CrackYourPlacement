class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def col_zero(m,j):
            for i in range(len(m)):
                m[i][j]=0

        def row_zero(m,i):
            for j in range(len(m[0])):
                m[i][j]=0
        
        c=copy.deepcopy(m)
        for i in range(len(c)):
            for j in range(len(c[0])):
                if c[i][j]==0:
                    row_zero(m,i)
                    col_zero(m,j)
