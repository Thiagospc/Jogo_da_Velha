from banner import b
from random import randrange # escolhas aleatórias
from colorama import Fore # estilos e cores de terminais
from time import sleep # time

# apresentação do programa
print("{}".format(Fore.BLUE + b + Fore.RESET))

sleep(1)

# variaveis do sistema
jogadas = 0
quem_joga = 2
maxjogadas = 9  

# variaveis do sistema
jogadas2 = 0
quem_joga2 = 2
maxjogadas2 = 9

velha = [
[' ',' ',' '],
[' ',' ',' '],
[' ',' ',' ']
]

def tela(): # parte gráfica do game
    global velha
    
    print(f"""
                                                C O L U N A
                                            
                                                0     1     2
                                        L    0:  {velha[0][0]} |  {velha[0][1]}  |  {velha[0][2]}
                                        I      ----|-----|----
                                        N    1:  {velha[1][0]} |  {velha[1][1]}  |  {velha[1][2]}
                                        H      ----|-----|----
                                        A    2:  {velha[2][0]} |  {velha[2][1]}  |  {velha[2][2]}
        \n""")
    print("                                                                                     Jogadas: {}".format(Fore.RED + str(jogadas) + Fore.RESET))

tela()

print("""
    [1] Singleplayer
    [2] Multiplayer
    [0] Sair
    """)
modo = int(input(":> "))
sleep(2)
# jogo
if modo == 1:    
    
    def jogador():
        global jogadas
        global quem_joga
        global maxjogadas
        
        if quem_joga == 2 and jogadas < maxjogadas:
            l = int(input("Linha :>"))
            c = int(input("Coluna :>"))
            
            
            while velha[l][c] != ' ':
                print(Fore.RED + "Locais preenchidos!!! jogue novamente" + Fore.RESET)
                l = int(input("Linha :>"))
                c = int(input("Coluna :>"))        
                
            velha[l][c] = 'X'
            quem_joga = 1
            jogadas += 1
            
    def cpu():
        global jogadas
        global quem_joga
        global maxjogadas    
        
        if quem_joga == 1 and jogadas < maxjogadas:
            l = randrange(0, 3)
            c = randrange(0, 3)
            
        
            while velha[l][c] != ' ':
                l = randrange(0, 3)
                c = randrange(0, 3)
            velha[l][c] = 'O'
            quem_joga = 2
            jogadas += 1
                    
        
    
                        
    while True:
        tela()
        jogador()
        if 'X' in velha[0][0] and 'X' in velha[0][1] and 'X' in velha[0][2]:
            tela()
            print("             O ganhador foi X(xis) \n")
            print()
            break
        elif 'X' in velha[1][0] and 'X' in velha[1][1] and 'X' in velha[1][2]:
            tela()
            print("             O ganhador foi X(xis)  \n")
            print()
            break
        elif 'X' in velha[2][0] and 'X' in velha[2][1] and 'X' in velha[2][2]:
            tela()
            print("             O ganhador foi X(xis)  \n")
            print()
            break
        else:
            pass
        # coluna
        if 'X' in velha[0][0] and 'X' in velha[1][0] and 'X' in velha[2][0]:
            tela()
            print("             O ganhador foi X(xis) \n")
            print()
            break
        elif 'X' in velha[0][1] and 'X' in velha[1][1] and 'X' in velha[2][1]:
            tela()
            print("             O ganhador foi X(xis)  \n")
            print()
            break
        elif 'X' in velha[0][2] and 'X' in velha[1][2] and 'X' in velha[2][2]:
            tela()
            print("             O ganhador foi X(xis)  \n")
            print()
            break
        else:
            pass
        # diagonais
        if 'X' in velha[0][0] and 'X' in velha[1][1] and 'X' in velha[2][2]:
            tela()
            print("             O ganhador foi X(xis)  \n")
            print()
            break
        elif 'X' in velha[0][2] and 'X' in velha[1][1] and 'X' in velha[2][0]:
            tela()
            print("             O ganhador foi X(xis)   \n")
            print()
            break
        # velha
        elif jogadas == maxjogadas:
            tela()
            print("             O jogo deu velha, hehehehehehe")
            break
        else:
            pass
        
        cpu()
        if 'O' in velha[0][0] and 'O' in velha[0][1] and 'O' in velha[0][2]:
            tela()
            print("             O ganhador foi O(bola)  \n")
            print()
            break
        elif 'O' in velha[1][0] and 'O' in velha[1][1] and 'O' in velha[1][2]:
            tela()
            print("             O ganhador foi O(bola)  \n")
            print()
            break
        elif 'O' in velha[2][0] and 'O' in velha[2][1] and 'O' in velha[2][2]:
            tela()
            print("             O ganhador foi O(bola)  \n")
            print()
            break
        else:
            pass
        # coluna
        if 'O' in velha[0][0] and 'O' in velha[1][0] and 'O' in velha[2][0]:
            tela()
            print("             O ganhador foi O(bola)  \n")
            print()
            break
        elif 'O' in velha[0][1] and 'O' in velha[1][1] and 'O' in velha[2][1]:
            tela()
            print("             O ganhador foi O(bola)  \n")
            print()
            break
        elif 'O' in velha[0][2] and 'O' in velha[1][2] and 'O' in velha[2][2]:
            tela()
            print("             O ganhador foi O(bola)  \n")
            print()
            break
        else:
            pass
        # diagonais
        if 'O' in velha[0][0] and 'O' in velha[1][1] and 'O' in velha[2][2]:
            tela()
            print("             O ganhador foi O(bola)  \n")
            print()
            break
        elif 'O' in velha[0][2] and 'O' in velha[1][1] and 'O' in velha[2][0]:
            tela()
            print("             O ganhador foi O(bola)  \n")
            print()
            break
        # velha
        elif jogadas == maxjogadas:
            tela()
            print("             O ganhador foi O(bola)  \n")
            break
        else:
            pass
        
# #####################################  

elif modo == 2:
    
    def jogador():
        global jogadas2
        global quem_joga2
        global maxjogadas2
    
        tela()
        
        if quem_joga2 == 2 and jogadas2 < maxjogadas2:
            l = int(input("Linha :>"))
            c = int(input("Coluna :>"))
            
            
            while velha[l][c] != ' ':
                print(Fore.RED + "Locais preenchidos!!! jogue novamente" + Fore.RESET)
                l = int(input("Linha :>"))
                c = int(input("Coluna :>"))        
                
            velha[l][c] = 'X'
            quem_joga2 = 1
            jogadas2 += 1
        
    def jogador2():
        global jogadas2
        global quem_joga2
        global maxjogadas2   
        
        tela() 
        
        if quem_joga2 == 1 and jogadas2 < maxjogadas2:
            l = int(input("Linha :>"))
            c = int(input("Coluna :>"))
            
            
            while velha[l][c] != ' ':
                print(Fore.RED + "Locais preenchidos!!! jogue novamente" + Fore.RESET)
                l = int(input("Linha :>"))
                c = int(input("Coluna :>"))        
                
            velha[l][c] = 'O'
            quem_joga2 = 2
            jogadas2 += 1
                    
        

                        
    while True:
        jogador()
        if 'X' in velha[0][0] and 'X' in velha[0][1] and 'X' in velha[0][2]:
            tela()
            print("             O ganhador foi X(xis) \n")
            print()
            break
        elif 'X' in velha[1][0] and 'X' in velha[1][1] and 'X' in velha[1][2]:
            tela()
            print("             O ganhador foi X(xis)  \n")
            print()
            break
        elif 'X' in velha[2][0] and 'X' in velha[2][1] and 'X' in velha[2][2]:
            tela()
            print("             O ganhador foi X(xis)  \n")
            print()
            break
       
        # coluna
        if 'X' in velha[0][0] and 'X' in velha[1][0] and 'X' in velha[2][0]:
            tela()
            print("             O ganhador foi X(xis) \n")
            print()
            break
        elif 'X' in velha[0][1] and 'X' in velha[1][1] and 'X' in velha[2][1]:
            tela()
            print("             O ganhador foi X(xis)  \n")
            print()
            break
        elif 'X' in velha[0][2] and 'X' in velha[1][2] and 'X' in velha[2][2]:
            tela()
            print("             O ganhador foi X(xis)  \n")
            print()
            break
        
        # diagonais
        if 'X' in velha[0][0] and 'X' in velha[1][1] and 'X' in velha[2][2]:
            tela()
            print("             O ganhador foi X(xis)  \n")
            print()
            break
        elif 'X' in velha[0][2] and 'X' in velha[1][1] and 'X' in velha[2][0]:
            tela()
            print("             O ganhador foi X(xis)   \n")
            print()
            break
        # velha
        elif jogadas2 == maxjogadas2:
            tela()
            print("             O jogo deu velha, hehehehehehe")
            print()
            break
       
        tela()
        jogador2()
        if 'O' in velha[0][0] and 'O' in velha[0][1] and 'O' in velha[0][2]:
            tela()
            print("             O ganhador foi O(bola)  \n")
            print()
            break
        elif 'O' in velha[1][0] and 'O' in velha[1][1] and 'O' in velha[1][2]:
            tela()
            print("             O ganhador foi O(bola)  \n")
            print()
            break
        elif 'O' in velha[2][0] and 'O' in velha[2][1] and 'O' in velha[2][2]:
            tela()
            print("             O ganhador foi O(bola)  \n")
            print()
            break
        
        # coluna
        if 'O' in velha[0][0] and 'O' in velha[1][0] and 'O' in velha[2][0]:
            tela()
            print("             O ganhador foi O(bola)  \n")
            print()
            break
        elif 'O' in velha[0][1] and 'O' in velha[1][1] and 'O' in velha[2][1]:
            tela()
            print("             O ganhador foi O(bola)  \n")
            print()
            break
        elif 'O' in velha[0][2] and 'O' in velha[1][2] and 'O' in velha[2][2]:
            tela()
            print("             O ganhador foi O(bola)  \n")
            print()
            break
        
        # diagonais
        if 'O' in velha[0][0] and 'O' in velha[1][1] and 'O' in velha[2][2]:
            tela()
            print("             O ganhador foi O(bola)  \n")
            print()
            break
        elif 'O' in velha[0][2] and 'O' in velha[1][1] and 'O' in velha[2][0]:
            tela()
            print("             O ganhador foi O(bola)  \n")
            print()
            break
        # velha
        elif jogadas2 == maxjogadas2:
            tela()
            print("             O jogo deu velha, hehehehehehe  \n")
            print()
            break
        


###########################################
elif modo == 0:
    print("Obrigado por usar o jogo")
    
else:
    print("Caractere inválido")
    
    
input("Digite ENTER para sair")