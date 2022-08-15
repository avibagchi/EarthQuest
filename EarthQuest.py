import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.utils import platform
from kivy.uix.widget import Widget
from kivy.clock import Clock


import time
import webbrowser
from csv import writer
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.lang import builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import csv
from pytextbelt import Textbelt
import requests
import smtplib
from email.message import EmailMessage
from random import randint
#import ee

#ee.Authenticate()
#ee.Initialize()


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "earthquest32@gmail.com"
    msg['from'] = user
    password = "cpbbptulakdzhwvi"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

class MainWindow (Screen):
  fullname=ObjectProperty (None)

  def btn (self):
      Registration()

class Registration(Screen):
   username = ObjectProperty(None)
   password = ObjectProperty(None)

   def btn(self):
       print(self.username.text, self.password.text)
       csv_registration(self.username.text, self.password.text)

class Login(Screen):
   username = ObjectProperty(None)
   password = ObjectProperty(None)

   def email_alert (self, subject,body,to):
       msg=EmailMessage ()
       msg.set_content (body)
       msg['subject']=subject
       msg['to']=to

       user="earthquest32@gmail.com"
       msg['from']=user
       password="cpbbptulakdzhwvi"

       server=smtplib.SMTP ("smtp.gmail.com",587)
       server.starttls()
       server.login (user,password)
       server.send_message(msg)
       server.quit ()

   def btn(self,user):
       x=verify_login(self.username.text, self.password.text)
       if x==True:
           print("Succesfful Login")
           with open('userinfo.csv', 'a') as fd:
              fd.write(user.text)
              fd.write(",")
           return True

       elif x==False:
           print("Incorrest Username or Password")
           return False
       #SecondWindow()


class SecondWindow (Screen):
  pass


class FourthWindow (Screen):
  city = ObjectProperty(None)
  state = ObjectProperty(None)
  code=ObjectProperty (None)
  character=ObjectProperty (None)


  def btn3 (self,city,state, code, character, phone):
      with open('userinfo.csv', 'a') as fd:
          fd.write(city.text)
          fd.write(",")
          fd.write(state.text)
          fd.write (",")
          fd.write (code.text)
          fd.write(",")
          fd.write (character.text)
          fd.write (",")
          fd.write (phone.text)
          fd.write("\n")
      #show_popup2()
      if code.text=="12211":
         webbrowser.open ("https://earth.google.com/web/data=Mj8KPQo7CiExVEtHNUZ6dXVYQUo0WkdOSkhaRFJ4c2RESFhHT1dyTVESFgoUMEFGQ0U4M0VBMDEzMDVGQUYzMkQ")


         #webbrowser.open_new("https://earth.google.com/web/data=Mj8KPQo7CiExVEtHNUZ6dXVYQUo0WkdOSkhaRFJ4c2RESFhHT1dyTVESFgoUMEFGQ0U4M0VBMDEzMDVGQUYzMkQ")
         #webbrowser.open("https://www.google.com/maps/place/" + city + ",+" + state)

class FifthWindow (Screen):

    def btn (self, namer, phrase):
        with open('userinfo.csv', 'r') as credentials:
            credentials_reader = csv.reader(credentials)
            iterstuffnew = iter(credentials_reader)
            next(iterstuffnew)
            for row in iterstuffnew:
                email_alert("EarthQuest: Message from " + namer.text, phrase.text, row[5] + "@vtext.com")


class Dice (Screen):
    num=ObjectProperty (None)

    def btn (self):
        self.num = randint(1, 12)
        self.num = str(self.num)

class SixthWindow (Screen):
    pass

class SeventhWindow (Screen):
    pass

class EigthWindow (Screen):
    pass
class NinthWindow (Screen):
    pass
class TenthWindow (Screen):
    pass
class EleventhWindow (Screen):
    pass
class TwelthWindow (Screen):
    pass
class ThirteenthWindow (Screen):
    pass
class FourteenthWindow (Screen):
    pass
class FifteenthWindow (Screen):
    pass
class Sheets (Screen):
    num = ObjectProperty(None)






class WindowManager (ScreenManager):
  pass

class P (FloatLayout):
  pass

class P2 (FloatLayout):
  pass

kv=Builder.load_file ("my.kv")

class MyMainApp (App):
  def build (self):
      return kv

def show_popup ():
  show=P()
  popupWindow=Popup (title="Chat", content=show, size_hint=(None, None), size= (400,400))
  popupWindow.open ()

def show_popup2 ():
  show=P2()
  popupWindow=Popup (title="Chat", content=show, size_hint=(None, None), size= (400,400))
  popupWindow.open ()


def csv_registration(username, password):

    #with open('credentials.csv', mode='w') as credentials:
        #credentials_writer = csv.writer(credentials, delimiter=',')
        #credentials_writer.writerow([username, password])
        #return

    with open('credentials.csv', 'a') as fd:
        fd.write(username)
        fd.write (",")
        fd.write (password)
        fd.write("\n")


def verify_login(username, password):
   login = False
   with open('credentials.csv', 'r') as credentials:
       credentials_reader = csv.reader(credentials)

       iterstuff = iter(credentials_reader)
       next(iterstuff)

       for row in iterstuff:
           if row[0]== username and row[1] == password:
               login = True
               break
   userID=str (username)
   if login==True:
       return True
   if login==False:
       return False

if __name__=="__main__":
  MyMainApp().run()
