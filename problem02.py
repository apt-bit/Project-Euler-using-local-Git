#Far too slow just using recursion

def main():
    fibs = [1,2]
    while True:
        nextfib = fibs[-1] + fibs[-2]
        if nextfib > 4000000:
            break
        fibs.append(nextfib)
    print('Sum of even fibonacci terms under four million: {}'.format(sum([fib for fib in fibs if fib%2==0])))

if __name__ == '__main__':
    main()
