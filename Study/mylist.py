book = "The Hitchhiiker's Guide to the Galaxy"
booklist = list(book)
#backwords = ''.join(booklist[len(booklist):0:-1])
backwords = ''.join(booklist[::-1])
# print(backwords)


vowels = set('aaeeiioouu')
# print(vowels)
word = input("Provide a word to search for vowels: ")
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)
