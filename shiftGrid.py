def shiftGrid(grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    """
    x = z = 0
    y = 2
    size = len(grid)
    check = []
    for i in grid:
        vector = i
        vector[0]=grid[(x+size-k)%size][len(grid[x])-1]
        for j in i:
            y+=1
            z+=1 
        x+=1
        y = 1
    return grid
grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(grid)
print(shiftGrid(grid, k))
print(grid)