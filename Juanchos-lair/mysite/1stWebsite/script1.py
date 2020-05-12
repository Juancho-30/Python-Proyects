from flask import Flask, render_template #Importing the flask class object

app = Flask(__name__) #Instatiating the Flask object 
                      #__name__ gets the name of the python script, it's a special variable

@app.route('/') #URL as homepage, can be changed
def home():
   return render_template("home.html")

@app.route('/about') #URL as homepage, can be changed
def about():
   return render_template("about.html")

if __name__=="__main__":
   app.run(debug=True)
