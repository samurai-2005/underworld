def remove(string, word):
    newstr= string.replace(word,"")
    return newstr.strip()

this="this is a new python program in which that that that i want to strip and remove some words"

n = remove(this, "that")
print(n)
    