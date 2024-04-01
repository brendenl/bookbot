def count_letters(string): 
    split = string.split()
    letterMap = {}
    for word in split:
        for letter in word:
            l = letter.lower()
            if l in letterMap:
                letterMap[l] += 1
            else:
                letterMap[l] = 1
    return letterMap

def main():
    with open('./books/frank.txt') as f:
        book = f.read()
        sorted_map = count_letters(book)
        arr = []
        for key in sorted_map:
            if(key.isalpha() == True):  
                arr.append((key, sorted_map[key]))
        arr.sort()
        print(arr)

if __name__ == '__main__':
    main()