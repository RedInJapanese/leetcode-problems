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
    #while(x<len(grid)):
    #    vector = grid[x]
    #    prev = grid[x][0]
    #    vector[0]=grid[(x+size-k)%size][len(grid[x])-1]
    #    vector[1]= prev
    #    while(y<len(grid[x])):
    #        #nex = grid[x][(y+k)%len(grid[x])]
    #        y+=1
    #        z+=1
    #        #print(nex)
    #    print(vector)
    #    x+=1
    #    y = 1
    toroidal=grid[(0+size-k)%size][len(grid[0])-1]
    for i in grid: 
        for j in i:
            prev = grid[x][(z+len(i)-1)%len(i)]
            check.append(prev)
            z+=1
        #print(check)
        grid[x] = check
        check = []
        x+=1
        z = 0
    for y in grid: 
        toroidal=grid[(z+size-k)%size][0]
        check.append(toroidal)
        z+=1
    z = 0
    for p in grid: 
        grid[z][0] = check[z]
        z+=1
    return grid
grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(grid)
print(shiftGrid(grid, k))
print(grid)