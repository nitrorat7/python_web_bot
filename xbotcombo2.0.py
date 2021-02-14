'''
WSKAZOWKI:
obsluga wyjatkow: https://selenium-python.readthedocs.io/api.html
action chains: -> .perform()
explicit waits -> czekamy az podanny element wyswietlli
sie na stronie: https://selenium-python.readthedocs.io/waits.html

POMYSLY:
page = requests.get(URLX) # to moze byc jedna zmiennna wstawiana do [...]
w BeautifulSoup([...] .text, "html.parser")
miejsce na logike switch -> goal: 01
on site button work with -> goal: 02

NIEWYKORZYSTANE IMPORTY:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

'''

import re
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#FRAZY
URLX = 'http://www.google.com/search?q=x-kom+msi+tomahawk+b550'
URLK = 'http://www.google.com/search?q=komputronik+msi+rtx+3080+x-gamin+trio'
#REQUESTY
komputronik = requests.get(URLK)
xkom = requests.get(URLX)
#ZMIENNE
soup = BeautifulSoup(xkom.text, "html.parser")
EUREKA = None
#PETLA SZUKAJACA 1 WYNIKU GOOGLE
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
#OSKROBANY LINK
EUREKA_LINK =  EUREKA[7:]
#INSTANCJA DRIVER
driver = webdriver.Firefox()
#IDZIEMY NA STRONE
driver.get(EUREKA_LINK)
if soup == BeautifulSoup(xkom.text, "html.parser"):
    try:
        #DODAJEMY PRODUKT
        driver.find_element_by_xpath('//*[@title="Dodaj do koszyka"]').click()
        time.sleep(5)
        #www.x-kom.pl/koszyk
        driver.find_element_by_xpath('/html/body/div[2]/div[10]/div/div/div/div[4]/a').click()
        time.sleep(5)

        #DO OPCJI DOSTAWY >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    #WYCHODZIMY
    finally:
        driver.quit()
elif soup == BeautifulSoup(komputronik.text, "html.parser"):
    pass
'''<button title="Dodaj do koszyka" 
class="sc-15ih3hi-0 sc-1smss4h-3 hvfWK sc-1hdxfw1-0 kVYHRg"
class="sc-1h16fat-0 sc-1v4lzt5-13 jipXcf sc-153gokr-0 kwClzl"><span
 class="sc-1hdxfw1-3 iKSSlW"><span class="sc-1tblmgq-0 sc-1tblmgq-3 fhWCKJ">
 <svg style="width: 100%;height: 100%;" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
 <path d="M8.5 16a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zm0 1a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3zm8-1a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zm0 1a1.5 1.5 0 1 0 0 3 1.5 1.5 
 0 0 0 0-3zM8 16h8.5v1H8v-1zm7.5-10V5h4.64l-2.25 9H7.5v-1h9.61l1.75-7H15.5zM5.093 4H2V3h3.907L8.59 16.888l-.979.203L5.093 4zM10 8h5v1h-5V8zm2-2h1v5h-1V6zM6 5h3v1H6V5z" fill="#FFF" 
 fill-rule="nonzero"></path></svg></span><span class="sc-1hdxfw1-1 khiICc">Dodaj do koszyka</span></span></button>'''