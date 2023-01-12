#!/usr/bin/env python
# coding: utf-8

# # Automação Web e Busca de Informações com Python
# 
# #### Desafio: 
# 
# Trabalhamos em uma importadora e o preço dos nossos produtos é vinculado a cotação de:
# - Dólar
# - Euro
# - Ouro
# 
# Precisamos pegar na internet, de forma automática, a cotação desses 3 itens e saber quanto devemos cobrar pelos nossos produtos, considerando uma margem de contribuição que temos na nossa base de dados.
# 
# Base de Dados: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=sharing
# 
# Para isso, vamos criar uma automação web:
# 
# - Usaremos o selenium
# - Importante: baixar o webdriver

# In[2]:


get_ipython().system('pip install selenium')


# In[1]:


get_ipython().system('pip install pyautogui')


# In[78]:


import pyautogui
import pandas as _pnds
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
        
browser = webdriver.Chrome() 
browser.get('https://www.google.com/')
browser.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')
browser.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
dolar = browser.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[3]/div/div[2]/input').get_attribute('value')

browser = webdriver.Chrome()
browser.get('https://google.com/')
browser.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
browser.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
euro = browser.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[3]/div/div[2]/input').get_attribute('value')

browser = webdriver.Chrome()
browser.get('https://www.melhorcambio.com/ouro-hoje')
gold = browser.find_element('xpath', '/html/body/div[5]/div[1]/div/div/input[2]').get_attribute('value')
gold = gold.replace(',', '.')
browser.quit()

table = _pnds.read_excel('Produtos.xlsx')

for index, value in enumerate(table):
        dolarIndex = []
        euroIndex = []
        goldIndex = []
        if value == 'Moeda':
            for elementIndex, element in enumerate(table[value]):
                if element == 'Dólar':
                    dolarIndex.append(elementIndex)
                if element == 'Euro':
                    euroIndex.append(elementIndex)
                else:
                    goldIndex.append(elementIndex)
            def findByIndex(coinsIndex):
                for coinIndex in coinsIndex:

table.loc[table['Moeda'] == 'Dólar', 'Cotação'] = float(dolar)
table.loc[table['Moeda'] == 'Euro', 'Cotação'] = float(euro)
table.loc[table['Moeda'] == 'Ouro', 'Cotação'] = float(gold)

table['Preço de Compra'] = table['Preço Original'] * table['Cotação']
table.to_excel('Produtos Novos.xlsx', index=False)
            
# display(table['Moeda'][2])
time.sleep(4)





# class WebDriver:
#     def __init__(self, get_url, browser_element_xpath, send_key, get_element_xpath, get_attribute_xpath):
#         self.get_url = get_url
#         self.browser_element_xpath = browser_element_xpath
#         self.send_key = send_key
#         self.get_element_xpath = get_element_xpath
#         self.get_attribute_xpath = get_attribute_xpath
    
#     def accessWebDriver(self): 
#         browser.get(self.get_url)
#         browser.find_element('xpath', self.browser_element_xpath).send_keys(send_key)
#         browser.find_element('xpath', self.browser_element_xpath).send_keys(Keys.ENTER)
#         return browser.find_element('xpath', self.get_element).get_attribute(get_attribute_xpath)


# ### Agora vamos atualiza a nossa base de preços com as novas cotações

# - Importando a base de dados

# In[45]:


import time
time.sleep(5)
print(pyautogui.position())


# - Atualizando os preços e o cálculo do Preço Final

# In[ ]:





# ### Agora vamos exportar a nova base de preços atualizada

# In[ ]:




