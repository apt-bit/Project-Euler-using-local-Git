def fib(n):
    fibs=[1,1]
    for i in range(n-2):
        fibs.append(fibs[i]+fibs[i+1])
    return fibs

def main():
    fibs = fib(10000)
    for n in fibs:
        if len(str(n))>=1000:
            print(fibs.index(n)+1)
            break

if __name__ == '__main__':
    main()
