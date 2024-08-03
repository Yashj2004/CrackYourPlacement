class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        n=len(points)
        res=-inf
        i=0
        last=0
        while i<n:
            if i>=last:
                last=i+1
            for j in range(last,n):
                if points[j][0]>k+points[i][0]:
                    break
                else:
                    ans=points[i][1]+points[j][1]+points[j][0]-points[i][0]
                    if ans > res:
                        res=ans
                        last=j
            i+=1
        return res
