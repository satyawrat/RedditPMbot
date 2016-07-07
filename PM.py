from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
import time

driver = webdriver.Chrome('/Users/satya/PycharmProjects/RedditPMbot/chromedriver')
driver.get('https://www.reddit.com/')

subject = "Special One Time Discount!"
message = """
YOUR MESSAGE BODY GOES HERE!
"""
wait = WebDriverWait(driver, 10)



# this is the code to login into reddit
username = driver.find_element_by_name('user')
username.send_keys('USERNAAME')
password = driver.find_element_by_name('passwd')
password.send_keys('PASSWORD')
password.send_keys('\n')

elem = wait.until(EC.element_to_be_clickable((By.ID,'mail')))
#driver.implicitly_wait(9)


with open('userlist.txt', 'r') as f:
    userlist = f.read().splitlines()
    for u in userlist:
        userurl = ("https://www.reddit.com/user/"+u)
        print userurl
        driver.get(userurl)
        elem = wait.until(EC.title_contains('overview'))
        elem = driver.find_element_by_link_text('send a private message')
        elem.click()
        elem = wait.until(EC.title_contains('messages:'))
        elem = driver.find_element_by_name('subject')
        elem.send_keys(subject+'\t'+message)
#        elem.send_keys('\t')
#        elem = driver.implicitly_wait(1)
#        elem.send_keys(message)
        delay = (randint(10,40))
        time.sleep(delay)
        elem = driver.find_element_by_name("send")
        elem.click()
        print time.ctime()




sudo = raw_input("What?")

#.until(EC.presence_of_element_located(browser.find_element_by_id('IdOfMyElement')))
#element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))