import time

from desktop import desk_abrir, desk_form
from script import web_login, web_valor, web_form
from api import conectarapi

def main():
    web_login()
    valor2 = web_valor()
    app =  desk_abrir(valor2)
    campo_valor = desk_form(app)
    web_form(campo_valor)
    dados_funcionario = conectarapi(valor2)
    app.kill()

    telefoneapi = dados_funcionario.get('phoneNumber')
    inicioapi = dados_funcionario.get('startDate')
    idapi = dados_funcionario.get('employeeID')



    nome, sobrenome, telefone, email, cidade, estado, postal, cargo, setor, inicio, gestor, enviar = web_form(app)

    time.sleep(1)
    nome.send_keys(campo_valor[0])
    sobrenome.send_keys(campo_valor[1])
    telefone.send_keys(telefoneapi)
    email.send_keys(campo_valor[2])
    cidade.send_keys(campo_valor[3])
    postal.send_keys(campo_valor[4])
    estado.send_keys(campo_valor[5])
    setor.send_keys(campo_valor[7])
    cargo.send_keys(campo_valor[8])
    inicio.send_keys(inicioapi)
    gestor.send_keys(campo_valor[6])
    time.sleep(1)

    enviar.click()

    input('Clique algo para continuar')

if __name__ == "__main__":
    try:
       main()


    except Exception as e:
        print(f"\nOcorreu um erro durante a orquestração: {e}")