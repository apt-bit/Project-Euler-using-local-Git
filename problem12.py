import math

def numdivisors(n):
    numofdivisors = 0
    squareroot = int(math.sqrt(n))
    for i in range(1, squareroot+1):
        if n%i==0:
            numofdivisors+=2
    if squareroot*squareroot == n:
        numofdivisors-=1
    return numofdivisors


def triangles(n):
    numbers=[1]
    for i in range(n):
        numbers.append(numbers[-1]+len(numbers)+1)
    return numbers


def main():
    t = triangles(100000)
    for n in t:
        if numdivisors(n)>500:
            number = n
            break
    print('first triangle number to have over 500 divisors: {}'.format(number))

if __name__ == '__main__':
    main()
