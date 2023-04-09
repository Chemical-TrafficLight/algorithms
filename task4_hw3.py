class Solution(object):
    def numIslands(self, grid):
        sq = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i, j) not in sq:
                    stack = [(i, j)]
                    sq.add((i, j))
                    while stack:
                        row, col = stack.pop()
                        for row_1, col_1 in (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1):
                            if 0 <= col_1 < len(grid[0]) and 0 <=row_1< len(grid)
                                    (row_1, col_1) not in sq) and grid[row_1][col_1] == "1":
                                stack.append((row_1, col_1))
                                sq.add((row_1, col_1))
                    count += 1
        return count