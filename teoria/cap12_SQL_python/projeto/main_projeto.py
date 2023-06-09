# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


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
pedidosData = dataFrame['Data_Pedido'].value_counts()
print(f"Os 20 dias com mais pedidos foram:\
      \n{pedidosData.head(20)}")

#Filtro/ano
filtro_anoPedido = dataFrame['ID_Pedido'].str.split('-').str[1].value_counts().sort_index()

# # Gráfico de barras
# plt.bar(filtro_anoPedido.index, filtro_anoPedido.values, label = 'Barras', color = 'red')
# plt.xlabel('Ano')
# plt.ylabel('Quantidade Vendida')
# plt.title('Quantidade vendida / Ano')
# plt.legend()
# plt.show()



"""
## Pergunta de Negócio 3:

### Qual o Total de Vendas por Estado?
Demonstre o resultado através de um gráfico de barras.
"""

print("\n\tExercicio 03\n")

vendaEstado = dataFrame.groupby('Estado')['ID_Pedido'].count().sort_values(ascending=False)
print(vendaEstado)

