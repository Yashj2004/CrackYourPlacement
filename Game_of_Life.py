class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row=len(board)
        col=len(board[0])

        res=[[-1 for x in range(col)] for y in range(row)]
        # print(res)
        for i in range(row):
            for j in range(col):
                count=0
                for m,n in [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j+1),(i+1,j+1),(i+1,j),(i+1,j-1),(i,j-1)]:
                    if 0<=m<row and 0<=n<col:
                        count+=board[m][n]

                if count<2:
                    res[i][j]=0
                    # print('c1')

                elif board[i][j]==1 and (count==2 or count==3):
                    res[i][j]=1
                    # print('c2')

                elif board[i][j]==1 and count>3:
                    res[i][j]=0
                    # print('c3')


                elif board[i][j]==0 and count==3:
                    res[i][j]=1
                    # print('c4')
                else:
                    res[i][j]=board[i][j]
                    # print('c5')
                print(count)
        # print(res)
        for i in range(row):
            for j in range(col):
                board[i][j]=res[i][j]
