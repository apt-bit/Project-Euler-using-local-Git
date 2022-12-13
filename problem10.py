def sieve(n):
    sieve=[True]*n
    sieve[0]=sieve[1]=False
    for i in range(len(sieve)):
        if sieve[i]:
            for j in range(i+i, len(sieve), i):
                sieve[j]=False
    return [i for i in range(len(sieve)) if sieve[i]]

if __name__ == '__main__':
    print(sum(sieve(2000000)))
