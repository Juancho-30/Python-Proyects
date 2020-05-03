myfile = open("files/fruits.txt")
#Save content in content vaiable, so that
#The cursor doesnt affect in the print,
#And you can print it as many times you want
content = myfile.read() #Reads the file with a cursor
myfile.close() #Closes the file

with open('file/fruits.txt', "w" ) as myfile:
    myfile.write("Tomato\nCcumber\nOnion") #Writing into a file, also it overwrites an existing file
    myfile.write("\nGarlic")
    content = myfile.read()

print(content)