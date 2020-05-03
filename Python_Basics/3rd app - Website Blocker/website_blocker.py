import time
from datetime import datetime as dt
temp = "hosts"
#hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "dub119.mail.live.com", "www.dub119.mail.live.com", "live.udlap.mx"]

while True:
   if dt(dt.now().year, dt.now().month, dt.now().day, 8 ) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16 ):
      
      print("Working hours.... ")
   else:
      print("FUN")
   time.sleep(5)
