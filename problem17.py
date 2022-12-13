
numberwords = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}
teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
ones = ['', 'one','two','three','four','five','six','seven','eight','nine']

def numtoword(n):
    #first attempt which I could'nt get to work so switched to if method
    word = ''
    thousandcount=0
    while n >= 1000:
        thousandcount+=1
        n -= 1000
    word += numberwords[thousandcount]+' thousand '

    hundredcount=0
    while n >= 100:
        hundredcount+=1
        n-=100
    word += numberwords[hundredcount]+' hundred and '

    tencount=0
    while n>=10:
        tencount+=1
        n-=10
    word+=numberwords[10*tencount] + ' '
    word+=numberwords[n]
    return word



def numtoword2(n):
    word = ''
    if len(str(n)) == 3:
        word += numberwords[int(str(n)[0])] + ' hundred'
        if (str(n)[1] != '0') and (str(n)[1] != '1'):
            word += ' and ' + tens[int(str(n)[1])] + ' ' + ones[int(str(n)[2])]
        elif str(n)[1] == '1':
            word += ' and ' + teens[int(str(n)[2])]
        elif str(n)[2] != '0':
            word += ' and ' + ones[int(str(n)[2])]

    elif len(str(n)) == 2:
        if str(n)[0] != '1':
            word += tens[int(str(n)[0])] + ones[int(str(n)[1])]
        if str(n)[0] == '1':
            word += teens[int(str(n)[1])]

    elif len(str(n)) == 1:
        word += ones[n]

    return word

def numtoword3(n):
    #now refactored a fair amount also this way is much more expandable
    n = str(n)
    word = ''
    if len(n) == 1:
        word += ones[int(n)]

    elif len(n) == 2:
        if n[0] != '1':
            word += tens[int(n[0])] + numtoword3(n[1:])
        if n[0] == '1':
            word += teens[int(n[1])]

    elif len(n) == 3:
        word += ones[int(n[0])] + ' hundred'
        if (n[1] == '0') and (n[2] == '0'):
            return word
        else:
            return word + ' and ' + numtoword3(n[1:])

    return word


if __name__ == '__main__':
    test2 = ''
    for i in range(1, 1000):
        test2 += numtoword3(i)
    test2 += 'one thousand'
    test2 = test2.replace(' ','')
    print(len(test2))
