# Projeto ChatBot Chico 🤖

O ChatBot é um projeto desenvolvido utilizando o Streamlit, uma biblioteca para criação de aplicativos web interativos com Python. Este bot oferece uma experiência de questionário interativo, onde os usuários podem responder a perguntas em um formato amigável. 

## Funcionalidades

- Convite Inicial: O bot cumprimenta o usuário e convida a participar de um questionário.

- Carregamento de Arquivo JSON: Os usuários podem carregar um arquivo JSON contendo perguntas e respostas para iniciar o questionário.

- Tipos de Perguntas: O questionário suporta diferentes tipos de perguntas, como verdadeiro/falso, múltipla escolha e perguntas abertas.

- Interatividade: O usuário interage com o bot selecionando respostas, e o bot fornece feedback durante o processo.

- Download de Respostas: Ao concluir o questionário, os usuários podem baixar um arquivo JSON contendo perguntas, respostas dadas e a pontuação obtida.

## Como Executar
1. Configure seu ambiente virtual:

    python -m venv myvenv
    source myvenv/bin/activate  # Para Unix/Linux
    .\myvenv\Scripts\activate   # Para Windows

2. Instale as dependências:

     ```bash
     - pip install streamlit

3. Execute o aplicativo
     ```bash
     streamlit run nome_do_aplicativo.py

4. Abra o aplicativo no local host gerado.

## Como Utilizar

-   Clique em "Sim" para aceitar o convite do questionário.
    Carregue um arquivo JSON com suas perguntas e respostas.
    Responda às perguntas apresentadas pelo bot.
    Ao concluir, visualize sua pontuação e baixe as respostas em um arquivo JSON.

## Personalização
Você pode personalizar o Bot Chico ajustando as perguntas, respostas e o formato do arquivo JSON. Sinta-se à vontade para modificar e expandir conforme suas necessidades.

**Observação:** Certifique-se de que o formato do arquivo JSON está de acordo com o esperado pelo código.
