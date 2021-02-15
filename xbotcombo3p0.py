#!/usr/bin/env python3
'''
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

POMYSLY:
page = requests.get(URLX) # to moze byc jedna zmiennna wstawiana do [...]
w BeautifulSoup([...] .text, "html.parser")
miejsce na logike switch -> goal: 01


NIEWYKORZYSTANE IMPORTY:
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
'''
import sys
import re
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
URLX = 'http://www.google.com/search?q=x-kom+msi+tomahawk+b550'
URLK = 'http://www.google.com/search?q=komputronik+msi+rtx+3080+x-gamin+trio'
xkom = URLX
komputronik = URLK
def funkcjazbiorcza():
    kierunek = xkom
    zupa = kierunekposzukiwan(kierunek)
    produkt = pierwszylink(zupa)
    udanaproba = probazakupuxkom(produkt)
    if udanaproba == False:
        kierunek = komputronik
        zupa = kierunekposzukiwan(kierunek)
        produkt = pierwszylink(zupa)
        #?
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

profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
driver = webdriver.Firefox(profile)

def probazakupuxkom(EUREKA_LINK):
    
    driver.get(EUREKA_LINK)
    try:
        #DODAJEMY PRODUKT
        driver.find_element_by_xpath('//*[@title="Dodaj do koszyka"]').click()
        time.sleep(2)
        #www.x-kom.pl/koszyk
        driver.find_element_by_css_selector('.sc-1v4lzt5-13').click()
        time.sleep(2)
        #przejdz do dostawy selektor .pvj85d-4 - > wspolny
        driver.find_element_by_css_selector(".pvj85d-4").click()
        #kontynuluj jako gosc
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/a[1]').click()
        #odbior osobisty w salonie x kom - zaznaczenie
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div/div[1]/div[2]/div/div[2]/div[1]/label/div[1]/span/span[1]').clikc()
        time.sleep(1)
        #akceptacja popup mozzilli
        allert = driver.switch_to_alert()
        allert.accept()
        #do listy salonow x kom -> na razie nie dziala
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div/div[1]/div[2]/div/div[2]/div[2]/div/div/button').click()
        time.sleep(1)
        '''
        /html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/a[1]
        kontynuluj jako gosc:
        dla ryzen 7 5800x:
         /html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/a[1] xpath
         a.rpxbpj-6:nth-child(2) -> css selector
         
        dla goodram ddr3:
        /html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/a[1]
        a.rpxbpj-6:nth-child(2) -> css selector 
        '''                 
        #DO OPCJI DOSTAWY >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        return True
        #WYCHODZIMY
    except:
        return False
        '''
        "przejd do dostawy" porownanie elementow dostepnych na tym etapie w xkom
        msi+tomahawk+b550  /html/body/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[3]/button
        selektor css .pvj85d-4
        goodram+ddr3 /html/body/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/button
        .pvj85d-4 oki'''         
        

def probazakupukomputornik(EUREKA_LINK):
    driver = webdriver.Firefox()
    driver.get(EUREKA_LINK)
    #inna logika bo inne przyciski

def main():
    funkcjazbiorcza()
    


main()
input('Press Enter to Continue...')
sys.exit()