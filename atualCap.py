import time
from selenium import webdriver

#Inicializando o driver do navegador Chrome
driver = webdriver.Chrome()
driver.maximize_window()
url_login = 'https://coinmarketcap.com/'
driver.get(url_login)

contador = 1
moeda = []
while contador <= 10:
    elemento_xpath_1 = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{contador}]/td[2]/p')
    if elemento_xpath_1.is_displayed():
        print(f'numero {contador} achado.')
        xpath2 = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{contador}]/td[3]/div/a/div/div/div/p')
        xpath3 = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{contador}]/td[8]/p/span[1]')
        textoNome = xpath2.text
        textoCap = xpath3.text
        moeda = {
            'Nome': textoNome,
            'Capitalização': textoCap
        }
        moedas.append(moeda)
        print(f'A moeda do ranking {contador} no mercado é {textoNome} com captalização de {textoCap}')
        contador += 1

print(f'Lista das top 10 moedas por capitalização: {moeda}')

Loading..
