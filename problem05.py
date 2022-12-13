"""
min for 10 is 7*5*3*2 = 210
max for 10 is 10! = 3628800 (not true since if divisible by ten then also divisible by 5 and 2)
go up in steps of 10
check 9 first then down can stop at 5

min for 20 is 19*17*13*11*7*5*3*2 = 9699690 (can also go up in steps of this since it must be a multiple of it)
max for 20 is 20! = 2432902008176640000 (can shorten this if computer takes too long)
    shortened to 24329020081766400 as if divisible by 20 then also divisible by 10, 5, and 2
only have to check down to 11 since all below that have already checked their multiples
"""
import math

primes = [2,3,5,7,11,13,17,19]

def finddivisible(divisor):
    minimum = math.prod([x for x in primes if x < divisor])
    for i in range(minimum, math.factorial(divisor), minimum):
        for j in range(divisor-1, int(divisor/2)-1, -1):
            if i%j == 0:
                if j == int(divisor/2):
                    return i
            else:
                break

def main():
    print(finddivisible(10))
    print(finddivisible(20))
    print(list(filter(lambda x : x < 10, primes)))

if __name__ == '__main__':
    main()
