"""
first way I did it was using the notsummable function but it was relatively slow
so I redid it using a sieve to record all divisor sums
"""

def d(n):
    return [i for i in range(1,int(n/2)+1) if n%i == 0]

def abundant():
    return [i for i in range(1,28124) if i < sum(d(i))]

def notsummable():
    abundants = abundant()
    sieve = [False]*28124
    for i in abundants:
        for j in abundants:
            if i+j < 28124:
                sieve[i+j] = True
    return [i for i in range(len(sieve)) if sieve[i] == False]

def notsummable2():
    #this is faster but not instant
    divisorsums = [0]*28124
    for i in range(1, len(divisorsums)):
        for j in range(i+i, len(divisorsums), i):
            divisorsums[j] += i
    abundants = [i for i in range(len(divisorsums)) if i < divisorsums[i]]
    sieve = [False]*28124
    for i in abundants:
        for j in abundants:
            if i+j < 28124:
                sieve[i+j] = True
    return sum([i for i in range(len(sieve)) if sieve[i] == False])

def main():
    print(notsummable2())

if __name__ == '__main__':
    main()
