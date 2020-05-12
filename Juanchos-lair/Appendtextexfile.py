with open('file/fruits.txt', "a+" ) as myfile: #Use w for write, r for read, x doesnt overwrite a file, a adds or appends to file
    #a+ for append and write, cursor goes to the end of the file
    myfile.write("\nOkra")
    myfile.seek(0) #Cursos will go to the 0 position
    content = myfile.read() # reads whatever is left of the file

print(content)
