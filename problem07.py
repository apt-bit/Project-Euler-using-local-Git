def makesieve(n):
    sieve = [True]*n
    sieve[0] = sieve[1] = False
    for i in range(len(sieve)):
        if sieve[i]:
            for j in range(i+i, len(sieve), i):
                sieve[j]=False
    return [i for i in range(len(sieve)) if sieve[i]]

def main():
    print('10001st prime is {}'.format(makesieve(1000000)[10000]))

if __name__ == '__main__':
    main()
