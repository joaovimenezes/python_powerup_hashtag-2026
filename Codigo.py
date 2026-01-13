# instalar bibliotecas
import pyautogui as pag
import pandas as pd
import time

#Passo 1: acessar o sistema

pag.PAUSE = 0.399
sistemlink = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
emaillogin = 'pythontest@gmail.com'
passwordlogin = 'hash'

# abrir navegador

pag.press('Win')
pag.write('Chrome')
pag.press('Enter')

time.sleep(0.4) #pausa de segurança

# abrir o site

pag.write(sistemlink)
pag.press('Enter')

time.sleep(2.1) #pausa para carregamento

#Passo 2: fazer login

pag.click(873, 469) #clicar no login

pag.write(emaillogin)
pag.press('Tab') #tab muda de item em um formulário
pag.write(passwordlogin)
pag.press('Tab')
pag.press('Enter')

time.sleep(3)

#Passo 3: abrir bd

tabela = pd.read_csv('produtos.csv')
print(tabela)

#Passo 4: cadastrar produto

for linha in tabela.index: #looping
    pag.click(873, 326)

    #codigo
    codigo = str(tabela.loc[linha, 'codigo'])
    pag.write(codigo)
    pag.press('Tab')

    #marca
    marca = str(tabela.loc[linha, 'marca'])
    pag.write(marca)
    pag.press('Tab')

    #tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pag.write(tipo)
    pag.press('Tab')

    #categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pag.write(categoria)
    pag.press('Tab')

    #preço
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pag.write(preco)
    pag.press('Tab')

    #custo
    custo = str(tabela.loc[linha, 'custo'])
    pag.write(custo)
    pag.press('Tab')

    #obsHashtag Camisa  
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan': #para nao dar erro cadastrand 'NaN'
        pag.write(obs)
    pag.press('Tab')

    pag.press('Enter')
    
    #scollar pra cima
    pag.scroll(1000)
