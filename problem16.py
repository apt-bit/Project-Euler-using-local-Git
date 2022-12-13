def main():
    return sum([int(n) for n in str(2**1000)])

if __name__ == '__main__':
    print('Sum of digits of 2^1000: {}'.format(main()))
