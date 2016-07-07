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
We are ModafinilDog.com and we are here to give you a special one-time discount on modafinil.


We beat every other modafinil vendor fair and square. Our prices are the best in the industry, and our customer support is even better!


We all know about Modafinil, and how it has helped thousands of people lead a better life. The whole world is talking about it. So I won't go into the details. Chances are, you have already used modafinil quite extensively yourself.

We are here to talk about our promise: **impeccable customer service, every single time.** You can reach us 24/7, via Phone (+1 40 88 44 42 88) or email (support@modafinildog.com).

**Payment Methods:** PayPal & Bitcoins.

    Every single order is guaranteed to be delivered to you in a timely manner. Your time is important, we help you save it.

We are only giving out discounts this one time.

**If you fail to lock-in on these prices, you will never find a better deal again.**

Use coupon code "mithrandir" to get a whopping 25% off!

All orders are covered under our **100% refund policy**, ensuring the best shopping experience.

Here is the price breakdown for **Modalert 200** with the discounts:

|    PILLS    | PRICE | PRICE PER PILL|
|:------------:|:---------:|:------------------:|
|100| $93| 0.93 cents|
|200| $150| 0.75 cents|
|300| $191| 0.63 cents|

We also offer 15% discount to repeat customers.


**Visit us at [ModafinilDog.com](https://modafinildog.com/) and save yourself time and money.**
"""
wait = WebDriverWait(driver, 10)



# this is the code to login into reddit
username = driver.find_element_by_name('user')
username.send_keys('21april1994')
password = driver.find_element_by_name('passwd')
password.send_keys('Thr0waway')
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