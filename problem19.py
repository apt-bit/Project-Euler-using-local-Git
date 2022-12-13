"""
0:mon
1:tues etc
1 jan 1900 was a monday
months: 31, 28/29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
first compute without leap years taken into account
"""

def sunday():
    sundaycount = 0
    day = 1 #first day of 1901 is a tuesday
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for year in range(1901, 2001):
        if (year %4 == 0):
            months[1] = 29
        for i in range(len(months)):
            day += months[i]
            day %= 7
            if day == 6:
                sundaycount+=1
        months[1] = 28

    print(day)
    print(sundaycount)


def main():
    sunday()

if __name__ == '__main__':
    main()
