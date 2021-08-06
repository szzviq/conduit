from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
# import pyperclip
import csv
# import ctypes

# copy          = ctypes.pythonapi._PyUnicode_Copy
# copy.argtypes = [ctypes.py_object]
# copy.restype  = ctypes.py_object

now = datetime.now()
act_time = now.strftime("%H%M")
mail = f'szzviq{act_time}@gmail.com'
reg_mail = copy(mail)
dummy_mail ='szzviq1754@gmail.com'
bad_password = 'nemjo'
password = 'Valami12'
username = f'User_new1754'

pict='https://thumbs.dreamstime.com/b/goth-girl-avatar-twin-tails-flat-74541563.jpg'
pict2 = "https://static.productionready.io/images/smiley-cyrus.jpg"
mod_mail=f'modositva{act_time}@gmail.com'
mod_username=f'mod_nev{act_time}'
mod_password='Valami13'
bio="Én vagyok a mesebeli okos lány, hoztam is, meg nem is..."

title = f"Story{act_time}"
about = "mese"
write = "Storytime"
tag = "mese"

title_mod = "Nem virágok W.H.Auden"
about_mod = "vers"
write_mod = "Festékfoltként sötétlik az ég. Valami esni fog. Nem eső, nem jég. És nem virágok"
tag_mod = "vers"
