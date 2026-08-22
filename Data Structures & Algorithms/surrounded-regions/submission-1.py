class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        # go through the connected 'O's and mark them '#' 
        # this is done for 'O's that can be reached from the edges
        def dfs(i, j):
            if i < 0 or j < 0 or i == rows or j == cols or board[i][j] != 'O':
                return
            board[i][j] = '#'
            for di, dj in directions:
                dfs(i + di, j + dj)

        # call for left and right columns
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        # call for top ad bottom rows
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # in the end, the leftover 'O's can be surrounded
        # and the '#'s need to be put back as we need to return the original board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'