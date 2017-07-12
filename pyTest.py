#import webbrowser
from sst.actions import *
import sst
import time

validator = 1
intervalos = 2



while validator == True:
  go_to('www.google.com')
  time.sleep(intervalos)
  print("proceso 2")
  time.sleep(intervalos)
  print("proceso 3")
  time.sleep(intervalos)
  #webbrowser.open("www.google.com")

input('aaaa')