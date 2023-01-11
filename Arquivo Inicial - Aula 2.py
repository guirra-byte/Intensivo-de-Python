#!/usr/bin/env python
# coding: utf-8

# In[80]:


get_ipython().system('pip install plotly')


# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# In[96]:


import pandas as _pnds
import math
import plotly.express as _plx

# Passo 1: Importaria a base de Dados
table = _pnds.read_csv('telecom_users.csv')
# Passo 2: Visualizar a base de Dados
    # - Entender as informações que você tem disponível
    # - Informações que não tem ajudam apenas te atrapalham;
table = table.drop('Unnamed: 0', axis=1)
# Passo 3: Tratamento de Dados
table['TotalGasto'] = _pnds.to_numeric(table['TotalGasto'], errors='coerce')
    # - Resolver arquivos que estão sendo reconhecidos de forma errada 
    # - Resolver valores vazio
        # - Removers colunas onde TODOS os valores são vazios
table = table.dropna(how='all', axis=1)
        # - Remover linhas onde ALGUNS valores estão vazios
table = table.dropna(how='any', axis=0)
display(table.info())


    
    # - Descobrir as cagadas da base de dados

# Passo 4: Análise de dados inicial
clientsQuantity = len(table['IDCliente'])
count = 0
for index, isChurn in enumerate(table['Churn']):
    if isChurn == 'Nao':
        count = count + 1
        if index == clientsQuantity - 1:
            churnClient = clientsQuantity - count
            
            clientQuantity = clientsQuantity
            churnClientQuantity = count
            
            unChurnClients = clientsQuantity - churnClientQuantity
            
            churnClients = clientsQuantity - unChurnClients  
            churnPercent = churnClient/clientsQuantity
            
            unChurnQuantity = clientsQuantity - churnClient
            unChurnPercent = unChurnQuantity/clientsQuantity
            
            
            print(f'''
            Finalizando análise...
            {round(churnPercent*100-0.5):,}% dos nossos clientes cancelaram a assinatura e
            {round(unChurnPercent*100-0.5):,}% continuam com a assinatura!''')
    else:
        continue;
    
# Passo 5: Análise detalhada - descobrir as causas do cancelamento
for inspect in table.columns:
    if inspect != 'IDCliente':
        graph = _plx.histogram(table, x=inspect, color='Churn', text_auto=True)
        graph.show()


# In[ ]:


def findUnChurnClient():
    for index, active in enumerate(table['Churn']):
        if active == 'Nao':
            unChurnClientIds = [table['IDCliente'][index]]
            unChurnClientIds.append(unChurnClientIds)
            
            activeClientsLength = len(table['IDCliente']
            if index == activeClientsLength:
                print(activeClientsLength)

def findById(id):
    clientIds = table['IDCliente']
    for clientId in clientIds:
        if clientId == id:
            print(f'Encontramos um user compatível: {id}')
                                      
for index, column in enumerate(table):
    for value in table[column]:
        number = _pnds.to_numeric(value, errors='coerce')
        isNaN = math.isnan(number)
        if isNaN == True:
            table = table.drop(table[column], axis=2) 
                                      


# ### Conclusões e Ações

# - Clientes que possuem famílias tendem a cancelar menos
#     - Promoções tamanho família
# - Clientes em seus primeiros meses de assinaturas tendem a cancelar menos
#     - Marketing muito agressivo
#     - Pode ser que a experiência tenha sido ruim durante o primeiro ano
#     - Podemos realizar uma promoção durante o primeiro ano 
# - Clientes não casados tendem a cancelar mais 
# - Algun problema na Internet de Fibra
# - Clientes que possuem proteção aos seus equipamentos tendem a cancelar mais
# - Clientes que não possuem suporte técnico tendem a cancelar mais
# - Clientes que possuem o plano mensal tendem a cancelar mais
#     - Realizar Marketing mais atrativo para outros planos (2 anos ou anual)
# - Clientes tendem a cancelar mais ao se depararem com o Boleto Eletronico
# 

# In[ ]:





# 
