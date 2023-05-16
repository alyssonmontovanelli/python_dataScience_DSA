''' PROJETO 01 '''

import random
from os import system, name

def limpa_tela(): 
    #windows
    if name == 'nt':
        _ = system('cls')
    #Mac ou Linux:
    else:
        _ = system('clean')

def boneco(x): #Apenas para estilizar o jogo
    estagio = [
        '''
            ____________
            |          |
            |          O
            |         \\|/
            |          | 
            |          |
            |         / \\
            | 
            |
            |
            -    
            
        ''',
        '''
            ____________
            |          |
            |          O
            |         \\|/
            |          | 
            |          |
            |           \\
            | 
            |
            |
            -    
            
        ''',
        '''
            ____________
            |          |
            |          O
            |         \\|/
            |          | 
            |          |
            |         
            | 
            |
            |
            -    
            
        ''',
        '''
            ____________
            |          |
            |          O
            |         \\|
            |          | 
            |          |
            |
            |
            |
            |
            -    
            
        ''',
        '''
            ____________
            |          |
            |          O
            |          |
            |          | 
            |          |
            |
            |
            |
            |
            -    
            
        ''',
        '''
            ____________
            |          |
            |          O
            |
            |
            |
            |
            |
            |
            |
            -    
            
        ''',
        '''
            ____________
            |          |
            |
            |
            |
            |
            |
            |
            |
            |
            -    
            
        ''',
    ]

    print(estagio[x])

def escolha(palavra):   
    letrasErradas = []
    chances = 6
    # list comprehension
    letrasDescobertas = ['_' for letra in palavra]
    #Diálogo
    while chances > 0:

        for tentativa in range(chances):
            
            boneco(chances)
            print(f"\n\tVocê possui {chances} chances.\
                \n\tAs letras erradas são: {letrasErradas}\
                \n\tA palavra que possui {len(letrasDescobertas)} letras é: {letrasDescobertas}")

            letraEscolhida = input("\nDigite uma letra: ").lower()
            # Tratativas de erros
            if len(letraEscolhida) == 1 and letraEscolhida != ' ' and letraEscolhida not in ['1','2','3','4','5','6','7','8','9','0']:
                if letraEscolhida in letrasErradas or letraEscolhida in letrasDescobertas:  
                    print(f"Letra {letraEscolhida} já foi escolhida antes, favor, escolha outra!")      
                else:
                    if letraEscolhida in palavra:
                        for i in range(len(palavra)):
                            if letraEscolhida == palavra[i]:
                                letrasDescobertas[i] = letraEscolhida
                               
                    else:
                        print(f"A letra '{letraEscolhida}' está incorreta, tente novamente!")
                        letrasErradas.append(letraEscolhida)
                        chances -= 1      
            else:
                print("Informe uma letra válida")
            
            if '_' not in letrasDescobertas:
                print(f"\n\n\tParabéns, você adivinhou a palavra '{palavra}'!\n\n")
                return 
    boneco(0)            
    print(f"\n\nVocê não adivinhou a palavra '{palavra}', portanto perdeu o jogo!\n\n")
                

def game():     
    limpa_tela()
    print("\nBem vindo(a) ao jogo da forca")
    print("Adivinhe a palavra a baixo\n")
    palavras = ['banana', 'melancia', 'uva', 'morango', 'laranja', 'abacate']
    palavra = random.choice(palavras)
    escolha(palavra)


#bloco main
if __name__ == "__main__":
    game()
















        
