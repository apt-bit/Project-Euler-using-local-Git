#solving the same way as problem 18

def reading():
    with open('constants\p067_triangle.txt') as f:
        lines = [(s.replace('\n', '')).split(' ') for s in f.readlines()]
    return [[int(i) for i in l] for l in lines]

def triangle(t):
    bottomcolumns = len(t[-1])
    rows = len(t)

    for i in range(rows-1, -1, -1):
        for j in range(0, bottomcolumns-1):
            t[i-1][j] = t[i-1][j] + max(t[i][j], t[i][j+1])
        bottomcolumns-=1

    return t[0][0]


def main():
    t = reading()
    print(triangle(t))

if __name__ == '__main__':
    main()
