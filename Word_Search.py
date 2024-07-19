class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, suffix):
            if len(suffix) == 0:
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != suffix[0]:
                return False
            temp = board[row][col]
            board[row][col] = "#"
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if backtrack(row + dr, col + dc, suffix[1:]):
                    return True
            board[row][col] = temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, word):
                    return True
        return False
