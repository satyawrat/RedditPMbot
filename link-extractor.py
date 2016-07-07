from lxml import html
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#file:///Users/satya/PycharmProjects/RedditPMbot/modadropship.html
#username=.(\w+)

with open('Nootropics.htm', 'r') as myfile:
    data=myfile.read().replace('\n', '')

userlist = re.findall(r"username=\"(\w+.\w+)", data)

print len(userlist)

with open('userlist.txt', 'a') as f:
    for s in userlist:
        f.write(s + '\n')