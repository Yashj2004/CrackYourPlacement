class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        r=len(grid)
        c=len(grid[0])
        ans=0
        def island(i,j):
            if i<0 or i>=r or j<0 or j>=c or grid[i][j]!='1':
                return
            grid[i][j]='0'
            island(i-1,j)
            island(i+1,j)
            island(i,j-1)
            island(i,j+1)
    
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='1':
                    island(i,j)
                    ans+=1
        return ans
