li = ["a","b","c","d","e"]

for index, letter in enumerate(li[:-1]):
    print index, letter,  "-", index + 1, li[index+1]
