import json
from difflib import get_close_matches

data = json.load(open("files/data.json")) #Uses json lib to open the data .json file

def translate(w): #Funtion for definition getting, gets the argument as w
    w = w.lower() #turns to lowercase 
    if w in data: #if the word exists in data, then...
        return data[w] #returns the value of the word (key:value)
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0: #The lenght of close matches list is greater than cero
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0]) #Substite the %s with the first close match
        if yn == "Y": #If yes
            return data[get_close_matches(w, data.keys())[0]]  #Returns the definition
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ") #Stores a word inputed by the user
output = translate(word) #sends the word argument
if type(output) == list: #If output is list
    for item in output:
        print(item) #Iterate in definition as list and print it
else:
    print(output) #If it is the string output it normally
