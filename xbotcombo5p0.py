#!/usr/bin/env python3
'''
obecnyURL = driver.get_url
driver.close() -> zamyka karte
driver.quit() -> wychodzi?

opis: bot zakupowy -> do sklepow komputronik i x-kom.
      jesli dany produkt jest dostepny,
      zostanie zakupiony i zamowiony do salonu.
      jesli jest niedostepny skryp ma sie przerwac.
      docelowo ma zostac zrobiony log do plixku txt, a takze
      zrzut ekranu zapisany w lokalizacji pliku skryptu.
Docelowa funkcjonalnosc skryptu: 
            -> SKRYPCIE ZSH(powloki) ZAINICJOWAC
             SKRYPT PYTHON, cyklicznie         
python3 -m xbotcombo... [bez .py] > output.txt ->zapisane nasze dziady a >> gdy majabyc nadpisane
dobrze jak skrypt bedzie w zmiennej srodowiskowej
if _name_ == _main_:
    bot()
(utworzyc klase bot)
rowniez sprawdzic _init_ itp itd:
petle zrobic jako metody klasy bot

#if name == main: ma za zadanie unikniecie global wariables ktore moglby wplynac zle na program

WSKAZOWKI:
obsluga wyjatkow: https://selenium-python.readthedocs.io/api.html
action chains: -> .perform()
explicit waits -> czekamy az podanny element wyswietlli
sie na stronie: https://selenium-python.readthedocs.io/waits.html

NIEWYKORZYSTANE IMPORTY:
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSwitchToTargetException
from selenium.common.exceptions import InvalidElementStateException
import sys
'''

import re
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

URLX = 'http://www.google.com/search?q=x-kom+ryzen7+5800x'
xkom = URLX
NAME_AND_SURNAME = "Daniel Janowczyk"
EMAIL = "danieljan@gmail.com"
PHONE = "552388984"

def funkcjazbiorcza(instancja):
    kierunek = xkom
    zupa = kierunekposzukiwan(kierunek)
    produkt = pierwszylink(zupa)
    probazakupuxkom(produkt, instancja)       
def kierunekposzukiwan(kierunek):
    page = requests.get(kierunek)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup
def pierwszylink(soup):
    EUREKA = None
    #PETLA SZUKAJACA 1 WYNIKU GOOGLE
    for tag in soup.findAll('a',href=True):
        link = tag['href']
        if re.search(r'/url*',link):
            print('eurekaXKOM')
            EUREKA = link
            break     
    #OSKROBANY LINK
    EUREKA_LINK =  EUREKA[7:]
    return EUREKA_LINK
def probazakupuxkom(EUREKA_LINK, driver):
    driver.get(EUREKA_LINK)
    time.sleep(1)
    #DODAJEMY PRODUKT
    driver.find_element_by_xpath('//*[@title="Dodaj do koszyka"]').click()
    time.sleep(2)
    #www.x-kom.pl/KOSZYK
    driver.find_element_by_css_selector('.sc-1v4lzt5-13').click()
    time.sleep(2)
    #przejdz do dostawy selektor
    driver.find_element_by_css_selector(".pvj85d-4").click()
    #kontynuluj jako gosc
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/a[1]').click()
    #odbior osobisty w salonie
    time.sleep(2)
    driver.find_element_by_css_selector('.sc-14rohpf-0').click()
    #wybierz salon z listy
    driver.find_element_by_css_selector('div.sc-1hndnir-2:nth-child(1) > button:nth-child(1)').click()
    #promenda
    driver.find_element_by_css_selector('div.sc-2jtv1t-6:nth-child(47) > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)').click()
    #platnosc przy odbiorze(bezplatnie)
    time.sleep(2)
    driver.find_element_by_css_selector('div.nhgagy-11:nth-child(5)').click()
    time.sleep(4)
    try:
    #Formularze wypelnione danymi     
        action = ActionChains(driver)
        action.send_keys(Keys.TAB)
        time.sleep(1)
        action.send_keys(Keys.TAB)
        time.sleep(1)
        action.send_keys(Keys.TAB)
        time.sleep(1)
        action.send_keys(Keys.TAB)
        action.send_keys(NAME_AND_SURNAME)#>>>>>>>> szybciej
        action.send_keys(Keys.TAB)
        action.send_keys(EMAIL)
        action.send_keys(Keys.TAB)
        action.send_keys(PHONE)
        # ->>>>>>>>>>>>>>> xxxddddfffFadsadsadasdsasd zjechac na dol strony myszka bo inaczej nie zobaczy sie elementu ptaszka itp itd
        action.perform()
        
        #zgoda odznaczona ptaszkiem
        zgoda = driver.find_element_by_css_selector('div.sc-1jh87d2-0:nth-child(1)') #-> czy dziala
        action.move_to_element(zgoda).click()
        #do poprawy
    except WebDriverException as wde: #mowi jaki blad wystapil
        aktualnylink = driver.current_url
        print("link do obecnej strony: ->   ",aktualnylink, '\n')
        print(wde)
        print("-----")
        print(str(wde))
        print("-----")
        print(wde.args)
        print(aktualnylink)
        time.sleep(5)
        #driver.quit()
def probazakupukomputornik(EUREKA_LINK):
    driver = webdriver.Firefox()
    driver.get(EUREKA_LINK)
def main():
    driver = webdriver.Firefox()
    user = driver
    funkcjazbiorcza(user)

main()
