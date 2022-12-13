def ispalin(n):
    n = str(n)
    for i in range(len(n)):
        if n[-i-1] == n[i]:
            continue
        else:
            return False
    return True

def findtwodigitproducts():
    twodigitnumbers = [i for i in range(10,100)]
    twodigitproducts = []
    for number in twodigitnumbers:
        for newnumber in twodigitnumbers:
            twodigitproducts.append(number*newnumber)
    twodigitproducts.sort()
    return twodigitproducts

def findthreedigitproducts():
    threedigitnumbers = [i for i in range(100,1000)]
    threedigitproducts = []
    for number in threedigitnumbers:
        for newnumber in threedigitnumbers:
            threedigitproducts.append(number*newnumber)
    threedigitproducts.sort()
    return threedigitproducts

def main():
    twodigitproducts = findtwodigitproducts()
    for i in range(len(twodigitproducts)):
        if ispalin(twodigitproducts[-i]):
            largestpalinfrom2 = twodigitproducts[-i]
            break
    threedigitproducts = findthreedigitproducts()
    for i in range(len(threedigitproducts)):
        if ispalin(threedigitproducts[-i]):
            largestpalinfrom3 = threedigitproducts[-i]
            break
    print('Largest palindrome made from the product of two 3-digit numbers is {}'.format(largestpalinfrom3))

if __name__ == '__main__':
    main()
