def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def SumOfDigits(n):
    return sum([int(i) for i in str(n)])

def main():
    print(SumOfDigits(factorial(100)))

if __name__ == "__main__":
    main()
