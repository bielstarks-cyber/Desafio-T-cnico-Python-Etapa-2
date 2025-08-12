import os

from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

load_dotenv(override=True)

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service = servico)

wait = WebDriverWait(navegador, 10)

def web_login():

        try:
            user_url = os.getenv('USER_URL')
            navegador.get(user_url)
            print("Acessou normalmente")
            navegador.find_element('xpath','//*[@id="button_modal-login-btn__iPh6x"]"]')
        except:
            navegador.refresh()

        navegador.find_element('xpath','//*[@id="onetrust-accept-btn-handler"]').click()
        navegador.find_element('xpath','//*[@id="button_modal-login-btn__iPh6x"]').click()

        campo_email = wait.until(
            EC.visibility_of_element_located(('xpath','/html/body/div[3]/div[3]/div/div[2]/div/div/div/div/div[1]/div[2]/div/input'))
                       )
        user_login = os.getenv('USER_LOGIN')
        navegador.find_element('xpath','/html/body/div[3]/div[3]/div/div[2]/div/div/div/div/div[1]/div[2]/div/input').send_keys(user_login)

        navegador.find_element('xpath', '/html/body/div[3]/div[3]/div/div[2]/div/div/div/div/div[1]/div[3]/button').click()

        campo_senha = wait.until(
            EC.visibility_of_element_located(('xpath','/html/body/div[3]/div[3]/div/div[2]/div/div/div/div/div[1]/div[3]/div/input'))
        )
        user_password = os.getenv('USER_SENHA')
        navegador.find_element('xpath', '/html/body/div[3]/div[3]/div/div[2]/div/div/div/div/div[1]/div[3]/div/input').send_keys(user_password)
        navegador.find_element('xpath','/html/body/div[3]/div[3]/div/div[2]/div/div/div/div/div[1]/div[4]/div/div[2]/button').click()

        campo_id = wait.until(
            EC.visibility_of_element_located(('xpath','/html/body/div[2]/div/form/div[1]/input'))
        )
        valor = navegador.find_element('xpath', '//html/body/div[2]/div/form/div[1]/input').get_attribute('value')


        campo_form = wait.until(
            EC.visibility_of_element_located(('xpath','//*[@id="startDate"]'))
        )


def web_valor():
    valor = navegador.find_element('xpath', '//html/body/div[2]/div/form/div[1]/input').get_attribute('value')


    return valor

def web_form(campo_valor):
    navegador.maximize_window()
    id = navegador.find_element('xpath','/html/body/div[2]/div/form/div[1]/input')
    navegador.execute_script("arguments[0].scrollIntoView();", id)
    nome = navegador.find_element('xpath','/html/body/div[2]/div/form/div[2]/div[1]/input')
    sobrenome = navegador.find_element('xpath','//*[@id="lastName"]')
    telefone = navegador.find_element('xpath','/html/body/div[2]/div/form/div[3]/div[1]/input')
    email = navegador.find_element('xpath', '/html/body/div[2]/div/form/div[3]/div[2]/input')
    cidade = navegador.find_element('xpath', '/html/body/div[2]/div/form/div[4]/div[1]/input')
    estado = navegador.find_element('xpath','/html/body/div[2]/div/form/div[4]/div[2]/select')
    postal = navegador.find_element('xpath','/html/body/div[2]/div/form/div[4]/div[3]/input')
    cargo = navegador.find_element('xpath','/html/body/div[2]/div/form/div[5]/div[1]/input')
    setor = navegador.find_element('xpath','/html/body/div[2]/div/form/div[5]/div[2]/select')
    inicio = navegador.find_element('xpath','/html/body/div[2]/div/form/div[6]/div[1]/input')
    gestor = navegador.find_element('xpath','/html/body/div[2]/div/form/div[6]/div[2]/input')
    enviar = navegador.find_element('xpath', '/html/body/div[2]/div/form/div[7]/div[1]/button')

    return nome, sobrenome, telefone, email, cidade, estado, postal, cargo, setor, inicio, gestor, enviar
