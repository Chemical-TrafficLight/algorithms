class Solution(object):
    def islandPerimeter(self, grid):
        perim = 0
        if len(grid) == 0:
            return 0
        #i по количеству элементов grid
        for i in range(len(grid)):
            #j по количеству элементов r
            for j in range(len(grid[i])):
                #если клетка равна 1
                if grid[i][j] == 1:
                    #общий периметр увеличивается на 4
                    perim += 4
                    #верхняя клетка
                    if i > 0 and grid[i - 1][j] == 1:
                        perim -= 2
                    #левая
                    if j > 0 and grid[i][j - 1] == 1:
                        perim -= 2
        return perim

