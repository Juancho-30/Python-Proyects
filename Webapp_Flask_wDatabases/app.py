from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)
#Set the value of dict key for the app knows where to look for database
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://user:pass@localhost/height_collector1'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://hcinkdjcmyfolh:753e3bd63badad1f9af4a18a445ef7c442f23e009acb67cc503161403a77789c@ec2-54-161-208-31.compute-1.amazonaws.com:5432/din8vup4hlv1?sslmode=require'
#?sslmode=require at the end for manipulating manually in computer DB
db=SQLAlchemy(app) #Specify the class object or blueprint

class Data(db.Model): #Model class of sqlalchemy object
   __tablename__="data"
   id=db.Column(db.Integer, primary_key=True)
   email_=db.Column(db.String(120), unique=True)
   height_=db.Column(db.Integer)

   def __init__(self, email_, height_):
      self.email_=email_
      self.height_=height_

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/success", methods=['POST']) #implicitly create GET method
def success():
   #Capture data by presing send button
   if request.method=='POST':
      email=request.form["email_name"]
      height=request.form["height_name"]

      if db.session.query(Data).filter(Data.email_== email).count() == 0: #checks if email already exists in the database, count = 0 if theres none
         data=Data(email,height) #Create object to map email and height
         db.session.add(data) #Add rows to table
         db.session.commit()
         average_height=db.session.query(func.avg(Data.height_)).scalar() #get average and store it as sql statement, then with scalar gets the number
         average_height=round(average_height,1) #round with one decimal point
         count=db.session.query(Data.height_).count() #Gets all the rows
         send_email(email, height, average_height, count)
         return render_template("success.html")

   return render_template("index.html", 
      text="Seems like that e-mail is already used!")

if __name__=='__main__':
   app.debug=True
   app.run()
