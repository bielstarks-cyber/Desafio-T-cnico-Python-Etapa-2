# Automação de Processo com Python e Selenium

Este projeto tem como objetivo automatizar um processo utilizando Python e a biblioteca Selenium.

---

## Pré-requisitos

Antes de iniciar, certifique-se de que os seguintes itens estão instalados e configurados no seu ambiente:

* **Executável do Sistema:** O arquivo `EmployeeList.exe` deve estar na raiz do disco local, em `C:\`.
* **Navegador:** [Google Chrome](https://www.google.com/chrome/) instalado e atualizado.
* **Python:** Versão 3.8 ou superior.

É altamente recomendado o uso de um **ambiente virtual (venv)** para isolar as dependências do projeto.

---

## Instalação

Siga os passos abaixo para configurar o ambiente e instalar as dependências necessárias.

1.  **Clone o repositório:**

    ```bash
    git clone <URL_DO_SEU_REPOSITORIO_AQUI>
    ```

2.  **Navegue até a pasta do projeto:**

    ```bash
    cd <NOME_DA_PASTA_DO_PROJETO>
    ```

3.  **(Opcional, mas recomendado) Crie e ative um ambiente virtual:**

    ```bash
    # Criar o ambiente
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    O arquivo `requirements.txt` contém todas as bibliotecas necessárias. Para instalá-las, execute o comando:

    ```bash
    pip install -r requirements.txt
    ```

---

## Como Executar

Com o ambiente devidamente configurado, você pode iniciar a automação.

1.  Certifique-se de que o executável `EmployeeList.exe` está em `C:\`.

2.  Execute o script principal do projeto (substitua `main.py` pelo nome do seu arquivo principal, se for diferente):

    ```bash
    python main.py
    ```

O script irá iniciar o navegador Chrome e começar o processo de automação.

---

## Tecnologias Utilizadas

* **Linguagem:** Python
* **Navegador Alvo:** Google Chrome
