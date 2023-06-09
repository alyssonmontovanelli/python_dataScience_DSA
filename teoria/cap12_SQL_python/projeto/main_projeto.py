# Imports
import numpy as np
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import re

dataFrame = pd.read_csv('dados\dataset.csv')
print(dataFrame.columns)


"""
Perguntas de negócio
"""

"""
Pergunta de Negócio 1:

Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?
"""

print("\n\tExercicio 01\n")

maiorVenda_OfSupplies = dataFrame[dataFrame['Categoria'] == 'Office Supplies'].groupby('Cidade')['Valor_Venda']\
                        .sum().sort_values(ascending= False) 

print(f"Resultado do exercicio 01:\
      \nCidade: {maiorVenda_OfSupplies.index[0]}\
      \nValor de venda: ${maiorVenda_OfSupplies[0]}\n\n")



"""
Pergunta de Negócio 2:

Qual o Total de Vendas Por Data do Pedido?
Demonstre o resultado através de um gráfico de barras.
"""

print("\n\tExercicio 02\n")
pedidosData = dataFrame.groupby('Data_Pedido')['Valor_Venda'].sum()
print(f"Os 20 dias com mais pedidos foram:\
      \n{pedidosData.head(20)}")

# plt.figure(figsize=(16,6))
# pedidosData.plot(x='Data_Pedido', y = 'Valor_Venda', color = 'orange') #Gráfico de barras com pandas
# plt.title('Quantidade vendida / Ano')
# plt.legend()
# plt.savefig('graphics\/exercicio_02_vendasPorData.png')
# plt.show()

#Filtro/ano
filtro_anoPedido = dataFrame['ID_Pedido'].str.split('-').str[1].value_counts().sort_index()

# # Gráfico de barras
# plt.bar(filtro_anoPedido.index, filtro_anoPedido.values, label = 'Barras', color = ('orange', 'grey'))
# plt.xlabel('Ano')
# plt.ylabel('Quantidade Vendida')
# plt.title('Quantidade vendida / Ano')
# plt.legend()
# plt.savefig('graphics\/exercicio_02_vendasPorAno.png')
# plt.show()



"""
## Pergunta de Negócio 3:

### Qual o Total de Vendas por Estado?
Demonstre o resultado através de um gráfico de barras.
"""

print("\n\tExercicio 03\n")

vendaEstado = dataFrame.groupby('Estado')['Valor_Venda'].sum().reset_index()
print(vendaEstado)

#Plotagem
# plt.figure(figsize=(16,8))
# sns.barplot(data = vendaEstado,
#             y = 'Valor_Venda',
#             x = 'Estado').set(title="Vendas Por Estado")
# plt.xticks(rotation = 80)
# plt.show()



'''
## Pergunta de Negócio 4:

### Quais São as 10 Cidades com Maior Total de Vendas?

Demonstre o resultado através de um gráfico de barras.
'''

print("\n\tExercicio 04\n")

vendas_porCidade = dataFrame.groupby('Cidade')['Valor_Venda'].sum().sort_values(ascending=False).reset_index().head(10)
print(vendas_porCidade)

#Plotagem
# plt.figure(figsize=(16,8))
# sns.barplot(data = vendas_porCidade,
#             y = 'Valor_Venda',
#             x = 'Cidade').set(title="10 Maiores Vendas Por Cidade")
# plt.ylabel('Valor total de vendas')
# plt.xlabel('Cidades')
# plt.xticks(rotation = 40)
# plt.show()



'''
## Pergunta de Negócio 5:

### Qual Segmento Teve o Maior Total de Vendas?

Demonstre o resultado através de um gráfico de pizza.
'''

print("\n\tExercicio 05\n")


vendas_porSegmento = dataFrame.groupby('Segmento')['Valor_Venda'].sum().reset_index()
print(f"Total de vendas por segmento\
      \n{vendas_porSegmento}")

#Plotagem
# plt.figure(figsize=(8,8))
# plt.pie(vendas_porSegmento['Valor_Venda'], labels = vendas_porSegmento['Segmento'], startangle = 60,autopct='%1.1f%%', shadow=True, explode = (0.1,0,0))
# plt.title('Vendas Por Segmento')
# plt.savefig('graphics\/exercicio_05_vendasPorSegmento.png')
# plt.show()



'''
## Pergunta de Negócio 6 (Desafio Nível Baby):

### Qual o Total de Vendas Por Segmento e Por Ano?
'''

print("\n\tExercicio 06\n")
#Utilizando regex e replace de string para alterar o id pedido para apenas ano
dataFrame['ID_Pedido'] = dataFrame['ID_Pedido'].apply(lambda x: re.sub(r'CA-(\d{4})-\d+', r'\1', x))
dataFrame['ID_Pedido'] = dataFrame['ID_Pedido'].apply(lambda x: re.sub(r'US-(\d{4})-\d+', r'\1', x))
# print(dataFrame.head(15))


vendas_porSegmentoAno = dataFrame.groupby(['ID_Pedido', 'Segmento'])['Valor_Venda'].sum()
print(f"O total de vendas, por Ano e Segmento, nos ultimos 4 anos foram:\
      \n{vendas_porSegmentoAno}")



'''
## Pergunta de Negócio 7 (Desafio Nível Júnior):

Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer uma simulação com
base na regra abaixo:

- Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
- Se o Valor_Venda for menor que 1000 recebe 10% de desconto.

### Quantas Vendas Receberiam 15% de Desconto?
'''
print("\n\tExercicio 07\n")

vendas_desconto15 = dataFrame[dataFrame['Valor_Venda'] >= 1000].Valor_Venda.count()
vendas_desconto10 = dataFrame[dataFrame['Valor_Venda'] < 1000].Valor_Venda.count()

print(f"{vendas_desconto15} vendas receberão o desconto de 15%.\
      \n{vendas_desconto10} vendas receberão o desconto de 10%.")



'''
## Pergunta de Negócio 8 (Desafio Nível Master):

### Considere Que a Empresa Decida Conceder o 
# Desconto de 15% do Item Anterior. Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?
'''
print("\n\tExercicio 08\n")

mediaAnterior = dataFrame['Valor_Venda'].mean().round(2)

tabela_copia = dataFrame.copy()
condicaoDesconto = tabela_copia['Valor_Venda'] >= 1000
teste = tabela_copia['Valor_Venda'].mean().round(2)
# tabela_copia['Valor_Venda'] = tabela_copia[tabela_copia['Valor_Venda'] >= 1000.00].apply(lambda x: x * 0.85)
# mediaFinal15 = tabela_copia['Valor_Venda'].mean().round(2)

# mediaFinal15 = dataFrame.loc[dataFrame['Valor_Venda'] >= 1000, 'Valor_Venda'].apply(lambda x: x * 0.85).mean().round(2)

# mediaFinal15 = dataFrame[dataFrame['Valor_Venda'] >= 1000].apply(lambda x: x*0.85)
print(mediaAnterior)
print(teste)
# print(condicaoDesconto)



'''
## Pergunta de Negócio 9 (Desafio Nível Master Ninja):

### Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?

Demonstre o resultado através de gráfico de linha.

'''





'''
## Pergunta de Negócio 10 (Desafio Nível Master Ninja das Galáxias):

### Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias? 

Demonstre tudo através de um único gráfico.
'''

print("\n\tExercicio 12\n")

vendas_12 = dataFrame.groupby(['Categoria', 'SubCategoria'])['Valor_Venda'].sum()
print(dataFrame['SubCategoria'].value_counts().head(12))
print(vendas_12)