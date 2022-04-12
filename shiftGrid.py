def shiftGrid(grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    """
    x = z = b = a = d = e =0
    size = len(grid)
    vector = []
    sorted = []
    grid2 = [] 
    for i in grid: 
        for j in i:
            vector.append(j)
            z+=1
        x+=1
    for i in vector: 
        prev = vector[(b + len(vector) - k) % len(vector)]
        sorted.append(prev)
        if(len(sorted) == len(grid[0])):
            print(sorted)
            grid2.append(sorted)
            sorted = []
        b+=1
    return grid2
grid = [[1],[2],[3],[4],[7],[6],[5]]
k = 23
print(grid)
shiftGrid(grid, k)
