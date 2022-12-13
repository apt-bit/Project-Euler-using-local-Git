def multiples3(n):
    return [i for i in range(3, n, 3)]

def multiples5(n):
    return [i for i in range(5, n, 5)]

def main():
    print('Sum of all multiples of 3 or 5 below 1000: {}'.format(sum(set(multiples3(1000)+multiples5(1000)))))

if __name__ == '__main__':
    main()
