#!/usr/bin/env python3

'''FUNKCJONALNOŚCI OCZEKIWANE:
jesli jest niedostepny skryp ma sie przerwac.
docelowo ma zostac zrobiony log do plixku txt, a takze
zrzut ekranu zapisany w lokalizacji pliku skryptu.
Docelowa funkcjonalnosc skryptu: 
-> SKRYPCIE ZSH(powloki) ZAINICJOWAC SKRYPT PYTHON, powtarzany

WSKAZOWKI:
obsluga wyjatkow: https://selenium-python.readthedocs.io/api.html
action chains: -> .perform()
explicit waits -> czekamy az podanny element wyswietlli
sie na stronie: https://selenium-python.readthedocs.io/waits.html
#if name == main: ma za zadanie unikniecie global wariables ktore moglby wplynac zle na program
python3 -m xbotcombo... [bez .py] > output.txt ->zapisane nasze dziady a >> gdy majabyc nadpisane
dobrze jak skrypt bedzie w zmiennej srodowiskowej
obecnyURL = driver.get_url
driver.close() -> zamyka karte
driver.quit() -> wychodzi?

NIEWYKORZYSTANE IMPORTY:
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSwitchToTargetException
from selenium.common.exceptions import InvalidElementStateException
import sys'''

'''
#ROBOCZE INPUTY
#TO POWINNO w zmienne URL 'http://www.google.com/search?q=x-kom+ , a zmienna XKOM powinna byc URL + poszukiwany_komponenet - ale to potem
imie_oraz_nazwisko = input('twoje imie(spacja)nazwisko')
poszukiwany_komponent = input('podaj produkt i frazy oddzielaj plusami')
adres_mailowy = input('podaj adres mailowy')
numer_telefonu = input('wprowadz numer telefonu')
#/ROBOCZE
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

URL = 'http://www.google.com/search?q=x-kom+thermal+grrizly+aeronaut+1g'
XKOM = URL
NAME_AND_SURNAME = "Daniel Janowczyk"
EMAIL = r'danieljan@gmail.com'
PHONE = "552388984"

def funkcjazbiorcza(instancja):
    kierunek = XKOM
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
            print('znaleziono link do x-kom')
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
    driver.find_element_by_css_selector('a.rpxbpj-6:nth-child(2)').click()
    #odbior osobisty w salonie /html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/a[1]
    time.sleep(2)
    driver.find_element_by_css_selector('.sc-14rohpf-0').click()
    #wybierz salon z listy
    driver.find_element_by_css_selector('div.sc-1hndnir-2:nth-child(1) > button:nth-child(1)').click()
    #promenda
    driver.find_element_by_css_selector('div.sc-2jtv1t-6:nth-child(47) > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)').click()
    #platnosc przy odbiorze(bezplatnie)
    time.sleep(2)
    pprzyodb = driver.find_element_by_css_selector('div.nhgagy-11:nth-child(5)')
    pprzyodb.click()
    try:
    #Wypelnienie danych i zgody 
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_DOWN)
        #tu sie zaczynaja wypelniac pola >>>>>>>> najwiekszy blad
        
        html.send_keys(Keys.TAB)
        time.sleep(1)
        html.send_keys(Keys.PAGE_DOWN * 2)
        time.sleep(4)
        pprzyodb.click()
        inp0 = driver.find_element_by_xpath("//input[@name='recipientName']")
        inp0.send_keys(NAME_AND_SURNAME)
        inp1 = driver.find_element_by_xpath("//input[@name='recipientEmail']")
        inp1.send_keys(EMAIL)
        inp2 = driver.find_element_by_xpath("//input[@name='recipientPhoneNumber']")
        inp2.send_keys(PHONE)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        regulamin = ActionChains(driver)
        freebird = driver.find_element_by_css_selector('div.sc-1jh87d2-0:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(2)') 
        regulamin.move_to_element(freebird)
        regulamin.click().perform()
    except WebDriverException as wde:
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
        #screenshot try xxxxxxxxxxxxxxxxxxx >>>>>>>>>>>>>>>>
    atleastfinalbutton = driver.find_element_by_xpath("//button[@class='sc-15ih3hi-0 pvj85d-4 ikdUhq']")
    atleastfinalbutton.click()
    time.sleep(3)
    try:
        finalbutton = driver.find_element_by_xpath("//button[@class='sc-15ih3hi-0 pvj85d-4 ikdUhq']")
        finalbutton.click()
        print("zakup udany")
        time.sleep(10)
        driver.save_screenshot('dowód_zakupu.png')
        driver.quit()
    except:
        print("zakup nieudany")
        driver.quit()
        
def probazakupukomputornik(EUREKA_LINK):
    driver = webdriver.Firefox()
    driver.get(EUREKA_LINK)
def main():
    driver = webdriver.Firefox()
    user = driver
    funkcjazbiorcza(user)

main()
