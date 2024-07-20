class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        r, c = len(matrix), len(matrix[0])
        hs = [0] * (c + 1) 
        ans = 0
        
        for row in matrix:
            for i in range(c):
                hs[i] = hs[i] + 1 if row[i] == '1' else 0
            s = []
            for i in range(len(hs)):
                while s and hs[i] < hs[s[-1]]:
                    h = hs[s.pop()]
                    w = i if not s else i - s[-1] - 1
                    ans = max(ans, h * w)
                s.append(i)
        
        return ans               
