# Webapp with Flask

POSTGRESQL with SQL ALCHEMY

```python

from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
#Set the value of dict key for the app knows where to look for database
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Azul.1995@localhost/height_collector1' 
db=SQLAlchemy(app) #Specify the class object or blueprint
class Data(db.Model): #Model class of sqlalchemy object
   __tablename__="data"
   id=db.Column(db.Integer, primary_key=True)
   email_=db.Column(db.String(120), unique=True)
   height_=db.Column(db.Integer)
   def __init__(self, email_, height_):
      self.email_=email_
      self.height_=height_


Then run on virtual env: 
Python
From app import db
Db.create_all() To create the Table
Or you can use in python method (Look for it)


Add data to table	@app.route("/")
	def index():
	   return render_template("index.html")
	@app.route("/success", methods=['POST']) #implicitly create GET method
	def success():
	   #Capture data by presing send button
	   if request.method=='POST':
	      email=request.form["email_name"]
	      height=request.form["height_name"]
	      print(email, height)
	      data=Data(email,height) #Create object to map email and height
	      db.session.add(data) #Add rows to table
	      db.session.commit()
	      return render_template("success.html")


```python


#To create a virtual environment need to use a clean installation of python, you can install there all the libraries that don-t want to install in the global 

Pip install virtualenv	To install virtual environment

Go to the directory and create a new folder:
Create the virtual environment:
Then on a terminal python -m venv <name for the folder of the venv>
Ejemplo: python -m venv virtual

Trigger python: virtual\Scripts\python
Virtual\Scripts\activate To use VENV

