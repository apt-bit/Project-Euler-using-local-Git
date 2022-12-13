import math

def findprimefactors(n):
    primefactors = []
    for i in range(2, int(math.sqrt(n))):
        while n%i == 0:
            n /= i  #currently makes floats, might be better to make int division to avoid rounding errors?
            primefactors.append(i)
    return primefactors

def main():
    print('Largest prime factor of 600851475143: {}'.format(max(findprimefactors(600851475143))))

if __name__ == '__main__':
    main()
