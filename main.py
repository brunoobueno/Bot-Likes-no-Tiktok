from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options 
import os
from os import system
import sys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def menu():
    browser.get("https://zefoy.com")
    browser.set_window_size(1920, 1080)
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button"))
    )
    browser.set_window_position(-10000, 0)
    likes()

def likes():
    while True:
        system("Titulo " + "TikTok Likes // Bot // por BrunoBueno")
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
        time.sleep(1)
        print("[+] Pagina Carregada")
        browser.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/div/input").send_keys(url)
        print("[+] Link Checado")
        time.sleep(1)
        try:
            print("[+] Verificando o Temporizador")
            time.sleep(1.3)
            browser.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/div/div/button").click()
            time.sleep(1.5)
            browser.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div[1]/div/form/button").click()
            print("[+] Curtidas enviadas com sucesso")
            browser.refresh()
            cls()
            seconds = 900
            while (1 < seconds):
                system("Titulo " + "TikTok Likes // Bot // por BrunoBueno")
                print("{} Segundos Restantes.".format(seconds))
                time.sleep(1)
                seconds = seconds - 1
                cls()
        except:
            cls()
            print("Você ainda está em cooldown! Tente novamente em alguns minutos.")
            browser.quit()
            input("\nPressione qualquer tecla para sair")
            sys.exit()

system("Titulo " + "TikTok Likes // por BrunoBueno")
url = input("Link? ")
if not "tiktok" in url:
    cls()
    system("Titulo " + "TikTok Likes // Error // por BrunoBueno")
    print("URL Inválida. Por Favor, Reunicie o Programa.")
    time.sleep(5)
    sys.exit()
time.sleep(1)
cls()
system("Titulo " + "TikTok Liker // Captcha // por BrunoBueno")
print("Por Favor, Resolva o captcha")
time.sleep(2)
browser = webdriver.Chrome(options=options)
menu()