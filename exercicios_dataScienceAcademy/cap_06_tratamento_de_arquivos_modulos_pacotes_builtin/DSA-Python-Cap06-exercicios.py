# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
lista = [15, 23, 69]

''' Primeira forma '''
listaRetorno = []
for n in lista:
    listaRetorno.append(n**3)
print(listaRetorno)

''' Segunda forma '''
elevaNum = list(map(lambda x: x**3, lista))
print(elevaNum)


# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
'''
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)
'''
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'.split()
resultado = list(map(lambda x: [x.upper(), x.lower(), len(x)], palavras))
print("\nExercício 02")
for i in resultado:
    print (i)


# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
print("\nExercício 03")
matriz1 = [[1, 2],[3,4],[5,6],[7,8]]
matriz2 = [[8, 9],[10,58],[64,11],[87,81]]
matriz3 = [[10, 20],[30,40],[50,60],[70,80]]

def transposta(matriz):
    novaLinha = []
    novaColuna = []
    matrizTransposta = []

    for linha in matriz:
        novaLinha.append(linha[0])
        novaColuna.append(linha[1])
    
    matrizTransposta.append(novaLinha)
    matrizTransposta.append(novaColuna)

    print(f"A matriz transposta da matriz solicitada é: {matrizTransposta}")
    
transposta(matriz1)
transposta(matriz2)
transposta(matriz3)


# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista4 = [0, 1, 2, 3, 4]

def multiplica(lista):
    listaQuadrada = list(map(lambda n: n**2, lista))
    listaCubo = list(map(lambda n: n**3, lista))

    print(f"\nExercício 04\
          \n\tA lista quadrada é: {listaQuadrada}\
      \n\te a lista elevada ao cubo é: {listaCubo}")
    
multiplica(lista4)


# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [10, 11, 12]

listaSoma = list(map(lambda x,y: x+y, listaA, listaB))
print(f"\nExercício 05\
      \n\tA lista com a soma das duas listas é: {listaSoma}")


# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar 
# apenas os valores negativos.
range(-5, 5)

valoresNegativos = list(filter(lambda x: x<0, range(-5,5)))
print(f"\nExercício 06\
      \n\tA lista com os valores negativos é: {valoresNegativos}")


# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

valoresComuns = list(filter(lambda x: x in b, a))
print(f"\nExercício 07\
      \n\tNúmeros comuns: {valoresComuns}")


# Exercício 8 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

def trocaValores(d1, d2):
    
    dictTemporiario = {}

    for d1Key, d2Val in zip(d1, d2.values()):
        dictTemporiario[d1Key] = d2Val
    
    print(f"\nExercício 08\
          \n\tNovo dicionário é: {dictTemporiario}")

trocaValores(dict1, dict2)


# Exercício 9 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista9 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

listaNova = []

for i, item in enumerate(lista9):
    if i > 5:
        listaNova.append(item)

print(f"\nExercício 09\
      \n\tNova lista: {listaNova}")


# Exercício 10 - Crie um regex em Python para extrair a palavra que aparece depois das palavras 
# Data e Science na frase: 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'
import re
texto = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'

palavras10 = re.findall(r'Data\s+(\w+)', texto)
palavras11 = re.findall(r'Science\s+(\w+)', texto)

print(palavras10)
print(palavras11)