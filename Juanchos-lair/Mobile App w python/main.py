#Import 3rd party dependencies
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.animation import Animation
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json, glob
from datetime import datetime
from pathlib import Path
import random

Builder.load_file('design.kv')


#Classes, that have to inherit from kivy imported objects
class LoginScreen(Screen):
   def sign_up(self):
      self.manager.current = "Sign_Up_Screen"

   def login(self,uname, pword):
      with open("users.json") as file:
         users = json.load(file) #dictionary containing users
      if uname in users and users[uname]['password'] == pword:
         self.manager.current = "Login_screen_success"
         self.manager.transition.direction = "left"
      else:
         self.ids.login_wrong.text = "Wrong username or password"




class RootWidget(ScreenManager):
   pass

class SignUpScreen(Screen):
   def add_user(self, uname, pword):
      with open("users.json") as file:
         users = json.load(file)
         users[uname] = {'username': uname,
                         'password': pword,
                         'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
      with open("users.json", 'w') as file:
         json.dump(users, file)
      self.manager.current  = "Sign_Up_Screen_success"

class SignUpScreenSuccess(Screen):
   def go_to_login(self):
      self.manager.transition.direction = "left"
      self.manager.current = "Login_screen"

class LoginScreenSuccess(Screen):
   def log_out(self):
      self.manager.transition.direction = "right"
      self.manager.current = "Login_screen"

   def get_quote(self, feel):
      feel = feel.lower()
      available_feelings = glob.glob("quotes/*txt")

      available_feelings = [Path(filename).stem for filename in
                              available_feelings]
      if feel in available_feelings:
         with open(f"quotes/{feel}.txt",encoding="utf8") as file:
            quotes = file.readlines() #List of all quotes
            #List of multiple strings, each string each quote
         self.ids.quote.text = random.choice(quotes)
      else: 
         self.ids.quote.text = "Try another feeling"

class ImageButton(ButtonBehavior, HoverBehavior, Image):
   pass

class MainApp(App): #Top hierarchy app
   def build(self):
      return RootWidget() #RootWidget object initializing

if __name__ =="__main__":
   MainApp().run() # run method of App inherited by MainApp