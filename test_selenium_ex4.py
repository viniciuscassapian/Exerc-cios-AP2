from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Pega o caminho do HTML na mesma pasta do script
caminho = os.path.abspath("ex4_modificado.html")

driver = webdriver.Chrome()
driver.get("file:///" + caminho.replace("\\", "/"))

# Preenchendo com os novos IDs e dados sugeridos
driver.find_element(By.ID, "input_nome").send_keys("Carlos Eduardo")
time.sleep(0.5)
driver.find_element(By.ID, "input_ra").send_keys("12345678")
time.sleep(0.5)
driver.find_element(By.ID, "nasc_dia").send_keys("15")
driver.find_element(By.ID, "nasc_mes").send_keys("05")
driver.find_element(By.ID, "nasc_ano").send_keys("1998")
time.sleep(0.5)
driver.find_element(By.ID, "select_curso").send_keys("Sistemas de Informação")
time.sleep(0.5)
driver.find_element(By.ID, "select_nota").send_keys("10")
time.sleep(0.5)
driver.find_element(By.ID, "txt_sugestoes").send_keys("Focar mais em testes de API.")
time.sleep(0.5)
driver.find_element(By.ID, "txt_obs").send_keys("Tudo funcionando!")
time.sleep(0.5)

driver.find_element(By.ID, "btn_enviar").click()
time.sleep(2)
print("Formulário enviado!")
driver.quit()
