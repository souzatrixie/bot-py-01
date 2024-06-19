import pyautogui as pausa
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class P002_Get_Values:
    def __init__(self):
        self.Navegador = webdriver.Chrome()

    def T01_Acessar_Site(self, url='https://www.google.com.br/'):
        self.Navegador.get(url)
        pausa.sleep(1)

    def T02_Buscar_Valor_Dolar(self):

        # Procurando pela barra de pesquisa e enviando 'Dólar hoje' como chave de pesquisa

        self.Navegador.find_element(By.NAME, 'q').send_keys("Dolar hoje")
        pausa.sleep(1)

        self.Navegador.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
        pausa.sleep(1)

        # Obtendo o valor do Dólar
        DolarValue = self.Navegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
        pausa.sleep(2)

        return DolarValue

    def T03_Buscar_Valor_Euro(self):

        # Limpando a barra de pesquisa e buscando por 'Euro hoje'

        self.Navegador.find_element(By.NAME, 'q').send_keys("")
        pausa.sleep(1)
        pausa.press('tab')
        pausa.sleep(1)
        pausa.press('enter')
        pausa.sleep(1)

        self.Navegador.find_element(By.NAME, 'q').send_keys("Euro hoje")
        pausa.sleep(1)

        self.Navegador.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
        pausa.sleep(1)
        
        # Obtendo o valor do Euro
        EuroValue = self.Navegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
        pausa.sleep(1)

        return EuroValue