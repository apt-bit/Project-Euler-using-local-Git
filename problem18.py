"""
find biggest sum when going from top of the triangle to bottom going through
adjacent numbers

my idea is to work bottom up, determining the biggest path that way will be
much less intensive and should be easier to code too
"""

def triangle():
    t = [[75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

    bottomcolumns = len(t[-1])
    rows = len(t)

    for i in range(rows-1, -1, -1):
        for j in range(0, bottomcolumns-1):
            t[i-1][j] = t[i-1][j] + max(t[i][j], t[i][j+1])
        bottomcolumns-=1

    return t[0][0]


def smalltri():
    l = [[3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
    ]
    """
    l[2][0] = l[2][0] + max(l[3][0], l[3][1])
    l[2][1] = l[2][1] + max(l[3][1], l[3][2])
    l[2][2] = l[2][2] + max(l[3][2], l[3][3])

    l[1][0] = l[1][0] + max(l[2][0], l[2][1])
    l[1][1] = l[1][1] + max(l[2][1], l[2][2])

    l[0][0] = l[0][0] + max(l[1][0], l[1][1])
    """
    k = 3
    for i in range(2, -1, -1):
        for j in range(0, k):
            l[i][j] = l[i][j] + max(l[i+1][j], l[i+1][j+1])
        k-=1

    return l[0][0]


def main():
    print(smalltri())
    print(triangle())

if __name__ == '__main__':
    main()
