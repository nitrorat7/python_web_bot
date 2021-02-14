'''dont mess with da robot'''

import re
import time
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
'''
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
#obsluga wyjatkow: https://selenium-python.readthedocs.io/api.html
#action chains: -> .perform()
#explicit waits -> czekamy az podanny element wyswietlli
#sie na stronie: https://selenium-python.readthedocs.io/waits.html

#frazy
URLX = 'http://www.google.com/search?q=x-kom+msi+gtx+1030'
URLK = 'http://www.google.com/search?q=komputronik+msi+rtx+3080+x-gamin+trio'
#requesty
komputronik = requests.get(URLK)
xkom = requests.get(URLX)

#page = requests.get(URLX) # to moze byc jedna zmiennna wstawiana do [...]
#w BeautifulSoup([...] .text, "html.parser")
# ''' miejsce na logike switch''' -> goal: 01
# on site button work with -> goal: 02

#zupa:
soup = BeautifulSoup(xkom.text, "html.parser")
EUREKA = None

for tag in soup.findAll('a',href=True):
    link = tag['href']
    if re.search(r'/url*',link) and soup == BeautifulSoup(xkom.text, "html.parser"):
        print('eurekaXKOM')
        EUREKA = link
        break
    elif re.search(r'/url*', link)  and soup == BeautifulSoup(komputronik.text, "html.parser"):
        print('eurekaKOMPUTRONIK')
        EUREKA = link
        break

#
EUREKA_LINK =  EUREKA[7:]

driver = webdriver.Firefox()
driver.get(EUREKA_LINK)
time.sleep(5)
driver.quit()
