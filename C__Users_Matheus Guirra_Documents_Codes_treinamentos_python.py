#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Automação de Sistemas e Processos com Python

### Desafio:

Todos os dias, o nosso sistema atualiza as vendas do dia anterior.
O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, assim que começar a trabalhar, com o faturamento e a quantidade de produtos vendidos no dia anterior

E-mail da diretoria: seugmail+diretoria@gmail.com<br>
Local onde o sistema disponibiliza as vendas do dia anterior: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing

Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado

### Desafio 02: 
Todos os dias, há novas interações nas redes sociais da empresa.
O seu trabalho como desenvolvedor é captar todas as interações e gerar um relatório, com as métricas de engajemento.


# In[2]:


get_ipython().system('pip install pyautogui')


# In[30]:


import pyautogui
import pyperclip
import time
import pandas as _pnds
from string import Template

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

# Desafio 01: 
    # Passo 01: Entrar no sistema da empresa (No link do drive); 
def awaitSleep(timeToSleep):
    time.sleep(timeToSleep)

def calcSalesIndicators():
    file = _pnds.read_excel(r'C:\Users\Matheus Guirra\Downloads\Vendas - Dez.xlsx')
    
    quantityTable = file['Quantidade']
    billingTable =  file['Valor Final']
    
    for index, quantity in enumerate(quantityTable):
        if index == 0:
            addQuantities = quantity + quantityTable[index + 1]
            addBilling = billingTable[index] + billingTable[index + 1]
        else:
            if quantityTable[index + 1] is not None:
                addQuantities = addQuantities + quantityTable[index + 1]
                addBilling = addBilling + billingTable[index + 1]
                if index == len(quantityTable):
                    print(addQuantities)
                    print(addBilling)
            else:
                break
            
def updateSales():
    pyautogui.hotkey('ctrl', 't')
    awaitSleep(5)
    
    pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter') 
    
    # Passo 02: Navegar até o local do relatório (Entrar na pasta Exportar);
    awaitSleep(5)
    pyautogui.click(x=2844, y=368, clicks=2)
    
    # Passo 03: Realizar o Download;
    awaitSleep(2)
    pyautogui.click(x=2854, y=548, clicks=1, interval=0.3)
    pyautogui.click(x=5334, y=245, clicks=1, interval=0.3)
    pyautogui.click(x=5096, y=791, clicks=1, interval=0.3)
    awaitSleep(5)
    
    # Passo 04: Calcular os indicadores (faturamento e quantidade de produtos);
    file = _pnds.read_excel(r'C:\Users\Matheus Guirra\Downloads\Vendas - Dez.xlsx')
    quantity = file['Quantidade'].sum()
    billing = file['Valor Final'].sum()
        
    # passo 05: Enviar email para a diretoria;
    pyautogui.hotkey('ctrl', 't')
    pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
    awaitSleep(5)
    
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    awaitSleep(5)
    
    pyautogui.click(x=2519, y=269, clicks=1)
    awaitSleep(2)
    
    pyautogui.click(x=4918, y=539, clicks=1)
    pyautogui.write('seugmail+diretoria@gmail.com', interval=0.20)
    awaitSleep(1.5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    
    pyperclip.copy('Relatório de vendas')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('tab')
    
    mailBody = f"""
    Prezados, bom dia
    
    O faturamento de ontem foi de: R${billing:,.2f}
    A quantidade de produtos vendidos foi de: {quantity:,}
    
    Abs
    Matheus Guirra<Son of God>
    """
    
    pyperclip.copy(mailBody)
    pyautogui.hotkey('ctrl', 'v')
    awaitSleep(2)
    
    pyautogui.hotkey('ctrl', 'enter')
    
updateSales()
    
# Desafio 02:
    # Passo 01: Realizar Login na rede social da empresa (No link do facebook);
    # Passo 02: Navegar até o local do relatóri o de métricas de engajemento;
    # Passo 03: Realizar o download do arquivo de métricas de engajemento da empresa;
    # Passo 04: Realizar a leitura do arquivo utilizando uma aplicação Node.Js (Cliques, Views, Likes...);
    # Passo 05: Enviar relatório para email do time de Marketing as 9h todos os dias (Cron Job);


# 

# In[ ]:





# In[ ]:





# ### Vamos agora ler o arquivo baixado para pegar os indicadores
# 
# - Faturamento
# - Quantidade de Produtos

# In[10]:


import pandas as _pnds

table = _pnds.read_excel(r'C:\Users\Matheus Guirra\Downloads\Vendas - Dez.xlsx')
print(table)


# ### Vamos agora enviar um e-mail pelo gmail

# In[ ]:


pyautogui.hotkey('ctrl', 't')
    pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
    awaitSleep(5)
    
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    awaitSleep(5)
    
    pyautogui.click(x=2519, y=269, clicks=1)
    awaitSleep(2)
    
    pyautogui.click(x=4918, y=539, clicks=1)
    pyautogui.write('seugmail+diretoria@gmail.com', interval=0.20)
    awaitSleep(1.5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    
    pyperclip.copy('Relatório de vendas')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('tab')
    
    mailBody = f"""
    Prezados, bom dia
    
    O faturamento de ontem foi de: R${billing:,.2f}
    A quantidade de produtos vendidos foi de: {quantity:,}
    
    Abs
    Matheus Guirra<Son of God>
    """
    
    pyperclip.copy(mailBody)
    pyautogui.hotkey('ctrl', 'v')
    awaitSleep(2)
    
    pyautogui.hotkey('ctrl', 'enter')


# #### Use esse código para descobrir qual a posição de um item que queira clicar
# 
# - Lembre-se: a posição na sua tela é diferente da posição na minha tela

# In[25]:


import time
import pyautogui
time.sleep(5)
print(pyautogui.position())


# In[ ]:





# In[ ]:




