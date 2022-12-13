def sumbignum():
    f = open('constants\\bignumberfor13.txt', 'r')
    n = [int(x) for x in f.read().split('\n')]
    f.close()

    print('First ten digits of sum: {}'.format(str(sum(n))[:10]))

if __name__ == '__main__':
    sumbignum()
