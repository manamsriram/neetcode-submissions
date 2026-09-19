class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        firstRow = False
        # we are using 0th row and column as markers
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        firstRow = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        # check column indicator first as we have a row marker already
        # if we do row marker first and column marker is not set, then 0, 0 becomes 0 incorrectly
        if matrix[0][0] == 0:
            for i in range(1, m):
                matrix[i][0] = 0

        if firstRow:
            for j in range(n):
                matrix[0][j] = 0
        