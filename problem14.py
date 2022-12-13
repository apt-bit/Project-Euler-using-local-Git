import functools
import sys

sys.setrecursionlimit(1500)

@functools.cache
def collatzrec(n, count=0):
    #takes too long to execute, approx 15 seconds
    if n==0:
        return 1
    if n==1:
        return count+1
    if n%2==0:
        return collatzrec(n/2, count+1)
    else:
        return collatzrec(3*n+1, count+1)

def chainlen():
    chainlengths=[]
    for i in range(1000000):
        chainlengths.append(collatzrec(i))
    print('Longest chain starting with a number under a million: {}, Length: {}'.format(chainlengths.index(max(chainlengths)), max(chainlengths)))

if __name__ == '__main__':
    chainlen()
