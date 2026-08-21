class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        # each set has points that can flow into pacific and atlantic respectively
        pac, atl = set(), set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, visit, prevHeight):
            # out of bounds, perviously visited or cannot flow
            if (r, c) in visit or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight:
                return
            visit.add((r, c))
            for i, j in directions:
                dfs(r + i, c + j, visit, heights[r][c])
    
        # check first row and last row
        for c in range(cols):
            # pass all points along with the pacific visit set as pacific is on top
            # we check in reverse how many points can reach the pacific.
            dfs(0, c, pac, heights[0][c])
            # last row close to atlantic
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        # check starting left and right columns
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res