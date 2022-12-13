def sumsquares(n):
    return sum([i*i for i in range(n+1)])

def squaresum(n):
    return sum([i for i in range(n+1)])**2

def main():
    print(squaresum(100)-sumsquares(100))

if __name__ == '__main__':
    main()
