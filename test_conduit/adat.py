# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
import time
from datetime import datetime
import csv

now = datetime.now()
act_time = now.strftime("%H%M")
#
# signup data

mail_1 = "testuser_1@ghail.com"
# bad_password = 'nemjo'
username = 'User_new1'
password = 'Valami12'

# data for new article
title = f"Story{act_time}"
about = "mese"
write = "Storytime"
tag = "mese"

# data for profile modification
pict = 'https://thumbs.dreamstime.com/b/goth-girl-avatar-twin-tails-flat-74541563.jpg'
# pict2 = "https://static.productionready.io/images/smiley-cyrus.jpg"
# mod_mail=f'modositva{act_time}@gmail.com'
mod_username = f'mod_nev{act_time}'
bio = "Én vagyok a mesebeli okos lány, hoztam is, meg nem is..."


#
# data for post modification
title_mod = "Nem virágok W.H.Auden"
about_mod = "vers"
write_mod = "Festékfoltként sötétlik az ég. Valami esni fog. Nem eső, nem jég. És nem virágok"
tag_mod = "vers"


def conduit_registration(driver):
    driver.find_element_by_xpath('//a[contains(text(),"Sign up")]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//input[contains(@placeholder,"Username")]').send_keys(username)
    driver.find_element_by_xpath('//input[contains(@placeholder,"Email")]').send_keys(mail_1)
    driver.find_element_by_xpath('//input[contains(@placeholder,"Password")]').send_keys(password)
    driver.find_element_by_xpath('//button[contains(@class,"pull-xs")]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]').click()
    time.sleep(5)


#

def conduit_signin(driver):
    driver.find_element_by_xpath('//a[contains(text(),"Sign in")]').click()
    driver.find_element_by_xpath('//input[contains(@placeholder,"Email")]').send_keys(mail_1)
    driver.find_element_by_xpath('//input[contains(@placeholder,"Password")]').send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath('//button[contains(@class,"pull-xs")]').click()


#
def conduit_new_article(driver):
    driver.find_element_by_xpath('//a[@href="#/editor"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//input[contains(@placeholder,"Article Title")]').send_keys(title)
    driver.find_element_by_xpath('//input[contains(@placeholder,"about")]').send_keys(about)
    driver.find_element_by_xpath('//textarea[contains(@placeholder,"Write your")]').send_keys(write)
    driver.find_element_by_xpath('//input[contains(@placeholder,"tags")]').send_keys(tag)
    driver.find_element_by_xpath('//button[contains(text(),"Publish")]').click()
