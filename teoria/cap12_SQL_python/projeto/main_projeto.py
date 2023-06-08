# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


dataFrame = pd.read_csv('dados\dataset.csv')



print(dataFrame.head())
print(dataFrame.shape)
print(dataFrame.describe())
print(dataFrame.tail())
print(dataFrame.columns)
print(dataFrame.isnull().sum())

"""
Perguntas de negócio
"""

"""
Pergunta de Negócio 1:

Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?
"""

print("\n\tExercicio 01\n")

maiorVenda_OfSupplies = dataFrame[dataFrame['Categoria'] == 'Office Supplies'].groupby('Cidade')['Valor_Venda'].sum().sort_values(ascending= False) 

print(f"Resultado do exercicio 01:\
      \nCidade: {maiorVenda_OfSupplies.index[0]}\
      \nValor de venda: ${maiorVenda_OfSupplies[0]}\n\n")