import time
from datetime import datetime as dt
#host_temp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"            
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "dub119.mail.live.com", "www.dub119.mail.live.com", "live.udlap.mx"]

while True:
   if dt(dt.now().year, dt.now().month, dt.now().day, 8 ) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16 ):
      
      print("Working hours.... ")
      with open(host_path, 'r+') as file: # r+ able to read and write
         content=file.read()
         for website in website_list:
            if website in content:
               pass
            else:
               file.write("\n"+redirect+" "+ website)
   else:
      with open(host_path, 'r+') as file:
         content=file.readlines() #Read as a list of string lines
         file.seek(0)
         for line in content:
            if not any(website in line for website in website_list):
               file.write(line)
            file.truncate()

      print("FUN")
   time.sleep(5)
