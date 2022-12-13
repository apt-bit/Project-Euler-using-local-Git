"""find how many routes through a lattice path

so have to remember where we are up to
also have to remember the entire route at the end as to not repeat
can only go right and down
so it always takes 4 movements for a 2x2 grid and 40 for 20x20

after looking online there is a cool idea of dynamically answering the problem
you look at the point next to the finish and say there is only one way to get to
the finish
then carry on moving back through the grid counting how many solutions there are from
each point adding on ones until you get back to the start.

NOTE: there are 21 points in a 20x20 grid

 ._._.
|._._.|
|._._.|

"""

#first for a 2x2 grid
#(has three rows of three points)
#all bottom and right edges have one route
def printgrid(g):
    for row in g:
        print(row)

def grid2x2():
    griddist = [
        [None,None,1],
        [None,None,1],
        [1,1,0]
    ]
    griddist[1][1] = griddist[1][2] + griddist[2][1]
    griddist[1][0] = griddist[1][1] + griddist[2][0]
    griddist[0][1] = griddist[0][2] + griddist[1][1]
    griddist[0][0] = griddist[0][1] + griddist[1][0]
    return griddist[0][0]
    #now to generalise this process

def grid2x2general():
    gridsize = 2
    grid = [[None for i in range(gridsize+1)] for j in range(gridsize+1)]
    #this is necessary for python to make new empty lists each time
    #more natural in python would probably be to use a grid indexed by 2-tuples
    # grid = {(x,y):0 for x in range(gridsize) for y in range(gridsize)}
    # will implement this in the 20x20
    grid[gridsize][gridsize]=0
    for i in range(gridsize):
        grid[i][gridsize] = 1
        grid[gridsize][i] = 1
    for i in range(gridsize-1, -1, -1):
        for j in range(gridsize-1, -1, -1):
            grid[i][j] = grid[i+1][j] + grid[i][j+1]
    return grid[0][0]

def grid20x20():
    gridsize = 20
    grid = {(x,y):0 for x in range(gridsize+1) for y in range(gridsize+1)}
    for i in range(gridsize):
        grid[i,gridsize] = 1
        grid[gridsize,i] = 1
    for i in range(gridsize-1, -1, -1):
        for j in range(gridsize-1, -1, -1):
            grid[i,j] = grid[i+1,j] + grid[i,j+1]
    return grid[0,0]


def main():
    print(grid20x20())

if __name__ == '__main__':
    main()
