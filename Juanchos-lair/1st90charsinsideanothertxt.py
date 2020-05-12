with open("bear.txt", "r") as bearfile:
    content = bearfile.read()
    with open("first.txt", "w") as myfile:
        myfile.write(content[:90])