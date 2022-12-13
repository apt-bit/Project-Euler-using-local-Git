

def alphabetical_position(a):
    return ord(a)-96

def name_value(name):
    value = 0
    for character in name:
        value += alphabetical_position(character)
    return value

def main():
    readingobject = open("constants\\namesfor22.txt","r")
    names = readingobject.read().split(",")
    names = [name.replace("\"","").lower() for name in names]
    names.sort()
    name_values = [name_value(name) for name in names]
    name_scores = []
    for i in range(len(name_values)):
        name_scores.append((i+1)*name_values[i])
    print('Total of all name scores: {}'.format(sum(name_scores)))

if __name__ == '__main__':
    main()
