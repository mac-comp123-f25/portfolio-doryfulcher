import string

def compute_frequencies(filename):
    file = open(filename, 'r')
    lines = file.read()
    print(lines)
    words = lines.split()
    clean_words =[]
    count = 0
    for word in words:
        newWord = word.strip(string.punctuation)
        clean_words.append(newWord)
        count = count + 1
    print(count)


compute_frequencies("../TextFiles/alice.txt")




