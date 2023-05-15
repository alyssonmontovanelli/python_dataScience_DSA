# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, 
# passando 2 parâmetros e depois faça uma chamada aos atributos e métodos
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)
        

''' Resolução 01'''
print("\n\tExercício 01\n")
roc1 = Rocket(5,9)

roc1.print_rocket()
roc1.move_rocket(20,30)
roc1.print_rocket()



# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

print("\n\tExercício 02\n")

class Pessoa():

    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

    def dados(self):
        print(f"\nDados de {self.nome}:\n\
              \nNome: {self.nome}\
              \ntelefone: {self.telefone}\
              \nEmail: {self.email}\
              \nCidade: {self.cidade}")

    def contato(self):
        print(f"\nTelefone para contato de {self.nome} é: {self.telefone}")

alysson = Pessoa("Alysson", "Três Corações", "(21) 99491-9345", "alysson@gmail.com")

alysson.dados()
alysson.contato()


# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

print("\n\tEXERCÍCIO 03:\n")
class Smartphone():
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface

class Mp3Player(Smartphone):
    def __init__(self, tamanho, interface, capacidade):
        Smartphone.__init__(self, tamanho, interface)
        self.capacidade = capacidade

mp3 = Mp3Player("15cm", "gráfica", "1TB")

print(mp3.tamanho)
print(mp3.interface)
print(mp3.capacidade)