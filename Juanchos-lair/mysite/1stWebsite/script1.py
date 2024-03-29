from flask import Flask, render_template #Importing the flask class object

app = Flask(__name__) #Instatiating the Flask object 
                      #__name__ gets the name of the python script, it's a special variable


@app.route('/plot/')
def plot():
   from pandas_datareader import data
   import datetime
   from bokeh.plotting import figure, show, output_file
   from bokeh.embed import components
   from bokeh.resources import CDN

   start=datetime.datetime(2019,3,1)
   end=datetime.datetime(2020,3,10)

   df = data.DataReader(name="GOOG", data_source="yahoo", start= start, end= end ) #Get data in that timeframe

   def inc_dec(c, o):
      if c > o:
         value="Increase"
      elif c < o:
         value="Decrease"
      else:
         value="Equal"
      return value

   df["Status"] = [inc_dec(c,o)  for c, o in zip(df.Close, df.Open)]
   df["Middle"]= (df.Open+df.Close)/2
   df["Height"]= abs(df.Close-df.Open)

   date_increase = df.index[df.Close > df.Open]
   date_decrease= df.index[df.Close < df.Open]
   p=figure(x_axis_type='datetime', width=1000, height=300, sizing_mode="scale_width")

   p.title.text = "Candlestick chart"
   p.grid.grid_line_alpha=0.7

   p.segment(df.index, df.High, df.index, df.Low, color="Black")

   hours_12 = 12*60*60*1000
   p.rect(df.index[df.Status=="Increase"], df.Middle[df.Status=="Increase"],
         hours_12, df.Height[df.Status=='Increase'],fill_color="#CCFFFF", line_color="black")

   p.rect(df.index[df.Status=="Decrease"], df.Middle[df.Status=="Decrease"],
         hours_12, df.Height[df.Status=='Decrease'],fill_color="#FF3333", line_color="black")

   
   script1, div1 = components(p) #tuple of js code, 2 elements 2nd element div

   cdn_js=CDN.js_files[0]
   return render_template("plot.html", 
   script1=script1,
   div1=div1, 
   cdn_js=cdn_js )

@app.route('/') #URL as homepage, can be changed
def home():
   return render_template("home.html")

@app.route('/about') #URL as homepage, can be changed
def about():
   return render_template("about.html")

if __name__=="__main__":
   app.run(debug=True)
