# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
from datetime import datetime

# import csv

#
#signup data
now = datetime.now()
act_time = now.strftime("%H%M")
# mail = f'szzviq{act_time}@gmail.com'
mail_1 = "testuser_1@ghail.com"
# bad_password = 'nemjo'
username = 'User_new1754'
password = 'Valami12'

#signin data
#dummy_mail ='szzviq1754@gmail.com'
# mail_for_mod_profile='nulltunder@ghail.com'

#data for new article
title = f"Story{act_time}"
about = "mese"
write = "Storytime"
tag = "mese"

#data for profile modification
# pict='https://thumbs.dreamstime.com/b/goth-girl-avatar-twin-tails-flat-74541563.jpg'
# pict2 = "https://static.productionready.io/images/smiley-cyrus.jpg"
# mod_mail=f'modositva{act_time}@gmail.com'
# mod_username=f'mod_nev{act_time}'
# mod_password='Valami13'
# bio="Én vagyok a mesebeli okos lány, hoztam is, meg nem is..."


#
#data for profile modification
# title_mod = "Nem virágok W.H.Auden"
# about_mod = "vers"
# write_mod = "Festékfoltként sötétlik az ég. Valami esni fog. Nem eső, nem jég. És nem virágok"
# tag_mod = "vers"


def conduit_registration(driver):
    driver.find_element_by_xpath('//a[contains(text(),"Sign up")]').click()
    driver.find_element_by_xpath('//input[contains(@placeholder,"Username")]').send_keys(username)
    driver.find_element_by_xpath('//input[contains(@placeholder,"Email")]').send_keys(mail_1)
    driver.find_element_by_xpath('//input[contains(@placeholder,"Password")]').send_keys(password)
    driver.find_element_by_xpath('//button[contains(@class,"pull-xs")]').click()
    driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]').click()
