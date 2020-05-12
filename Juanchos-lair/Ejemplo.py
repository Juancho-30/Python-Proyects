with open('files/data.txt', "a+" ) as datafile: #si lo abres con append, el cursor se va al ultimo
    datafile.seek(0)
    content = datafile.read()
    datafile.seek(0)
    datafile.write(content)
    datafile.write(content)
