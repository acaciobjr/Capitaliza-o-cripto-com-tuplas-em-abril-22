from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.coingecko.com/")
driver.maximize_window()

marcador2 = int(input('até que numero do top 100 você deseja trazer?'))

marcador = 1
while marcador < marcador2:

    xpath = f'//html/body/div[2]/main/div/div[5]/table/tbody/tr[{marcador}]/td[3]/a/div/div'
    preco = f'//html/body/div[2]/main/div/div[5]/table/tbody/tr[{marcador}]/td[11]/span'
    element = driver.find_element(By.XPATH, xpath)
    element2 = driver.find_element(By.XPATH, preco)
    huhu = element.text
    hyhy = element2.text 
    
    print(f'a criptomoeda numero {marcador} é {huhu} com {hyhy} de capitalização.')
    marcador += 1
