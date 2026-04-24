from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def abrir_html():
    caminho = os.path.abspath("ex3.html")
    driver = webdriver.Chrome()
    driver.get("file:///" + caminho.replace("\\", "/"))
    return driver

def test_exercicio01():
    driver = abrir_html()
    titulo = driver.title
    print("Título:", titulo)
    assert titulo == "Exercicio 3"
    paragrafo = driver.find_element(By.TAG_NAME, "p")
    assert paragrafo.text == "O conteúdo do site vem aqui"
    driver.quit()
