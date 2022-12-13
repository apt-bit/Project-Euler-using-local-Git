import math

def horizontal(grid):
    fours = []
    for i in range(len(grid)-3):
        newfour = []
        for j in range(4):
            newfour.append(grid[i+j])
        fours.append(math.prod(newfour))
    return fours

def vertical(grid):
    fours = []
    for i in range(len(grid)-60):
        newfour = []
        for j in range(0, 61, 20):
            newfour.append(grid[i+j])
        fours.append(math.prod(newfour))
    return fours

def diagonallyright(grid):
    fours = []
    for i in range(len(grid)-63):
        newfour =[]
        for j in range(0, 64, 21):
            newfour.append(grid[i+j])
        fours.append(math.prod(newfour))
    return fours

def diagonallyleft(grid):
    fours = []
    for i in range(4, len(grid)-60):
        newfour = []
        for j in range(0, 58, 19):
            newfour.append(grid[i+j])
        fours.append(math.prod(newfour))
    return fours

def main():
    f = open('constants\\gridfor11.txt', 'r')
    grid = f.read()
    f.close()
    grid = [int(i) for i in grid.replace('\n',' ').split(' ')]
    products = [max(horizontal(grid)), max(vertical(grid)), max(diagonallyright(grid)), max(diagonallyleft(grid))]
    print('largest product of four adjacent numbers: {}'.format(max(products)))

if __name__ == '__main__':
    main()
