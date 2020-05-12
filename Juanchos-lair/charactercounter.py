def foo(character, filepath="bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)

#Counts the number of characters from a given argument, in a .txt