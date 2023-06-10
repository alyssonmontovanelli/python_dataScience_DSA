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


vendas_porSegmento = dataFrame.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(by= 'Valor_Venda', ascending=False)
print(f"Total de vendas por segmento\
      \n{vendas_porSegmento}")

# Formatando para melhor visualização - valor em notação apra absoluto
def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v = val)
    return my_format


#Plotagem ----
# plt.figure(figsize=(8,8))
# plt.pie(vendas_porSegmento['Valor_Venda'], labels = vendas_porSegmento['Segmento'], startangle = 60,autopct='%1.1f%%', shadow=True, explode = (0.1,0,0))
# plt.title('Vendas Por Segmento')
# plt.savefig('graphics\/exercicio_05_vendasPorSegmento.png')
# plt.show()

# #Plotagem 2 'Turbinada DSA' ---
# plt.figure(figsize=(16,6))
# plt.pie(vendas_porSegmento['Valor_Venda'], labels = vendas_porSegmento['Segmento'], startangle = 90,\
#         autopct= autopct_format(vendas_porSegmento['Valor_Venda']))
# #Limpa circulo Central
# center_circle = plt.Circle((0,0), 0.82, fc = 'white')
# fig = plt.gcf()
# fig.gca().add_artist(center_circle)
# #Labels e anotações
# plt.annotate(text = 'Total de Vendas ' + '$ ' + str(int(sum(vendas_porSegmento['Valor_Venda']))), xy = (-0.25,0))
# plt.title('Total de Vendas Por Segmento')
# plt.show()





'''
## Pergunta de Negócio 6 (Desafio Nível Baby):

### Qual o Total de Vendas Por Segmento e Por Ano?
'''

print("\n\tExercicio 06\n")
#Utilizando regex e replace de string para alterar o id pedido para apenas ano
dataFrame['ID_Pedido'] = dataFrame['ID_Pedido'].apply(lambda x: re.sub(r'CA-(\d{4})-\d+', r'\1', x))
dataFrame['ID_Pedido'] = dataFrame['ID_Pedido'].apply(lambda x: re.sub(r'US-(\d{4})-\d+', r'\1', x))

vendas_porSegmentoAno = dataFrame.groupby(['ID_Pedido', 'Segmento'])['Valor_Venda'].sum()
print(f"O total de vendas, por Ano e Segmento, nos ultimos 4 anos foram:\
      \n{vendas_porSegmentoAno}")

# Outra forma de fazer, com datetime
dataFrame['Data_Pedido'] = pd.to_datetime(dataFrame['Data_Pedido'], dayfirst = True) # com isso o tipo da coluna vira datetime64
# Criando nova coluna 'ano'
dataFrame['Ano'] = dataFrame['Data_Pedido'].dt.year
vendas_porSegmentoAno2 = dataFrame.groupby(['Ano', 'Segmento'])['Valor_Venda'].sum()
print(vendas_porSegmentoAno2)




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

#Condicional com np.where - se for maior que 1000, desconto será de 0.15
dataFrame['Desconto'] = np.where(dataFrame['Valor_Venda'] >= 1000, 0.15, 0.10)

dataFrame['Valor_Venda_Final'] = dataFrame['Valor_Venda'] - (dataFrame['Valor_Venda'] * dataFrame['Desconto'])

valor_semDesconto10 = dataFrame[dataFrame['Desconto'] == 0.1].Valor_Venda.sum()
valor_comDesconto15 = dataFrame[dataFrame['Desconto'] == 0.15].Valor_Venda_Final.sum()
valor_medioFinal_desconto_15 = (valor_semDesconto10 + valor_comDesconto15) / dataFrame['Valor_Venda'].count()

print(f"Valor medio, sem aplicar os descontos de 15% fica em: $ {dataFrame['Valor_Venda'].mean().round(2)}")
print(f"\nValor medio, com aplicacao dos descontos de 15% fica em: $ {round(valor_medioFinal_desconto_15,2)}\n")




'''
## Pergunta de Negócio 9 (Desafio Nível Master Ninja):

### Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?

Demonstre o resultado através de gráfico de linha.

'''
dataFrame['Mes'] = dataFrame['Data_Pedido'].dt.month

# relplot para relacionar diferentes

media_ano_mes_segmento = dataFrame.groupby(['Ano', 'Mes', 'Segmento'])['Valor_Venda'].agg([np.sum, np.mean, np.median])

anos = media_ano_mes_segmento.index.get_level_values(0)
meses = media_ano_mes_segmento.index.get_level_values(1)
segmentos = media_ano_mes_segmento.index.get_level_values(2)

# plt.figure(figsize=(12,6))
# sns.set()
# fig1 = sns.relplot(kind='line',
#                   data=media_ano_mes_segmento,
#                   y = 'mean',
#                   x = meses,
#                   hue = segmentos,
#                   col = anos,
#                   col_wrap = 2)
# plt.ylabel('Valor Médio')
# plt.show()

# sns.kdeplot(media2015, x='Mes', y=media2015.values)
# plt.xlabel('sdahu')
# plt.show()



'''
## Pergunta de Negócio 10 (Desafio Nível Master Ninja das Galáxias):

### Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias? 

Demonstre tudo através de um único gráfico.
'''

# Criando DF
total_vendas_Cat_top12SubCat = dataFrame.groupby(['Categoria',
                                                  'SubCategoria']).sum(numeric_only=True).sort_values('Valor_Venda',
                                                                                                      ascending=False).head(12)

# Convertendo coluna Valor_Venda em num inteiro e classificando por cat
total_vendas = total_vendas_Cat_top12SubCat[['Valor_Venda']].astype(int).sort_values(by= 'Categoria').reset_index()

# DatafRAME com totais por categoria para anel exterior
total_vendas_Cat = total_vendas.groupby('Categoria').sum(numeric_only= True).reset_index()

print(total_vendas)
print(total_vendas_Cat)

# Cores para categorias

cores_categorias = ['#5d00de',
                    '#0ee84f',
                    '#e80e27',]

cores_subCategorias = ['#aa8cd4',
                       '#aa8cd5',
                       '#aa8cd6',
                       '#26c957',
                       '#26c958',
                       '#26c959',
                       '#26c960',
                       '#e65e65',
                       '#e65e66',
                       '#e65e67',
                       '#e65e68',]

#Plotagem

fig, ax = plt.subplots(figsize=(16,10))

# gráfico categorias
grafico1 = ax.pie(total_vendas_Cat['Valor_Venda'],
            radius=1,
            labels = total_vendas_Cat['Categoria'],
            wedgeprops= dict(edgecolor = 'white'), #limite das divisoes
            colors = cores_categorias)

# gráfico subcategorias
grafico2 = ax.pie(total_vendas['Valor_Venda'],
                  radius = 0.9,
                  labels= total_vendas['SubCategoria'],
                  autopct = autopct_format(total_vendas['Valor_Venda']),
                  colors = cores_subCategorias,
                  labeldistance = 0.7,
                  wedgeprops= dict(edgecolor = 'white'),
                  pctdistance= 0.53,
                  rotatelabels = True) # legendas tortas

#Limpra o centro do circulo

centre_circle = plt.Circle((0,0), 0.6, fc = 'white')

# Labels e anotações
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(total_vendas['Valor_Venda']))),xy = (-0.2, 0))
plt.title('Total de Vendas Por Categoria e Top 12 SubCategorias')
plt.show()