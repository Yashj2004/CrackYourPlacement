class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])


        def fill_value(borad,row,col,pre,next):
            if row < 0 or row > m-1 or col<0 or col>n-1:
                return 
            if board[row][col]!=pre:
                return
            board[row][col]=next

            fill_value(board,row-1,col,'-','O')
            fill_value(board,row+1,col,'-','O')
            fill_value(board,row,col+1,'-','O')
            fill_value(board,row,col-1,'-','O')



        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='-'


        for i in range(n):
            if board[0][i]=='-':
                fill_value(board,0,i,'-','O')

        for i in range(n):
            if board[m-1][i]=='-':
                fill_value(board,m-1,i,'-','O')

        for i in range(m):
            if board[i][0]=='-':
                fill_value(board,i,0,'-','O')

        for i in range(m):
            if board[i][n-1]=='-':
                fill_value(board,i,n-1,'-','O')


        for i in range(m):
            for j in range(n):
                if board[i][j]=='-':
                    board[i][j]='X'
            
            
