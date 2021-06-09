# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 13:21:23 2021

@author: Poulami
"""

import urllib.request, urllib.error
#import bs4
#import plyer
from bs4 import BeautifulSoup
import datetime
from plyer import notification
import time


def WordOfTheDay(f):
  content=f.read()
  soup = BeautifulSoup(content,'lxml')
  word_html=soup.findAll("div",{'class':"word-and-pronunciation"})
  defination_html=soup.findAll("div",{'class':"wod-definition-container"})
  for x in word_html:
    word=(x.find('h1').text)
    break
  definition=[]
  for x in defination_html:
    for col in x.find_all('p'):
      if ':' in col.text[0:6]:
        definition.append(col.text)
    definition_val="\n".join(definition)
  while (True):
    notification.notify(
    #title of the notification,
    title = "Word Of The Day For {}: {}".format(datetime.date.today().strftime("%d, %b %Y"),word.upper()),
    #the body of the notification
    message = "Definition: {defi}".format(defi=definition_val),  
    #creating icon for the notification
    #we need to download a icon of ico file format
    app_icon = "Bell.ico",
    # the notification stays for 50sec
    timeout  = 60
    )
    #sleep for 4 hrs => 60*60*4 sec
    #notification repeats after every 4hrs
    time.sleep(60*60*4)

if __name__=="__main__":
  url = 'https://www.merriam-webster.com/word-of-the-day'
  try:
      conn = urllib.request.urlopen(url)
  except urllib.error.HTTPError as e:
      # Return code error (e.g. 404, 501, ...)
      # ...
      print('HTTPError: {}'.format(e.code))
  except urllib.error.URLError as e:
      # Not an HTTP-specific error (e.g. connection refused)
      # ...
      print('URLError: {}'.format(e.reason))
  else:
      # 200
      # ...
      WordOfTheDay(conn)