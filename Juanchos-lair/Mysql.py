import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect()
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter a word: ")
query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word) #Select all from the table dictionary
results = cursor.fetchall() #Extracts as a list of tuples [(Term, definition)]
if results:
    for result in results:
        print(result[1]) #Of each tuple gets the definition
else:
        print("No word found!")