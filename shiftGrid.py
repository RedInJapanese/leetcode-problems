def shiftGrid(grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    """
    x = z = 0
    y = 2
    size = len(grid)
    vector = []
    for i in grid: 
        toroidal=grid[(x+size-k)%size][len(grid[x])-1]
        for j in i:
            prev = grid[x][(z+len(i))%len(i)]
            vector.append(j)
            z+=1
        print(vector)
        vector = []
        x+=1
grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(grid)
shiftGrid(grid, k)
print(grid)