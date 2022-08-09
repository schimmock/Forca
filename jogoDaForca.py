from re import A
import time 
import os


erros = 0
digitadas = []
Desafiante = str(input("Nome do desafiante: "))
Competidor = str(input("Nome do competidor: "))
time.sleep(1)
os.system ("cls") 
palavraChave = str(input("Palavra chave: "))
dica1 = str(input("dica1: "))
dica2 = str(input("dica2: "))
dica3 = str(input("dica3: "))
time.sleep(1)
os.system ("cls") 



def pergunta ():
    print("Jogar = 1")
    print("Solicitar Dica = 2")


'''def jogar ():
    
    while True:
        letra = str(input("digite uma letra: "))
        if letra not in palavraChave:
            erros = erros + (1)

        if len in (letra) > "1":
            print("mais de uma vez!")  
    
        digitadas.append(letra)
        
        segredo = ""
        for letra in palavraChave:
            if letra in digitadas:
                segredo += letra
            else:
                segredo += "*"
               
        if segredo == palavraChave:
            print("Parabéns,", Competidor, "você ganhou!")
            break
        else:
            print("A palavra no momento se encontra assim:", (segredo))
            print(erros)
            break '''
         
        

for len in (palavraChave):
    print ("*")
while True:  
    loop = ()
    while True:
        if loop == ():      
            pergunta()
            resposta = int(input( ))
            if resposta == 1:
                print ("vamos la")
                time.sleep(1)
                os.system ("cls") 
                while True:
                    letra = str(input("digite uma letra: "))
                    if letra not in palavraChave:
                        erros = erros + (1)

                    if len in (letra) > "1":
                        print("mais de uma vez!")  
                
                    digitadas.append(letra)
                    
                    segredo = ""
                    for letra in palavraChave:
                        if letra in digitadas:
                            segredo += letra
                        else:
                            segredo += "*"
                        
                    if segredo == palavraChave:
                        print("Parabéns,", Competidor, "você ganhou!")
                        arquivo = open("registro.partida", "w")
                        arquivo.write(palavraChave)
                        arquivo.write("/n")
                        arquivo.write(Competidor)
                        arquivo.write("/n")
                        arquivo.write(Desafiante)
                        arquivo.close
                        break
                    if erros >= 5:
                        print("Vitória do desafiante! parabéns", Desafiante)
                        arquivo = open("registro.partida", "w")
                        arquivo.write("Palavra:", palavraChave, "vencedor desafiante:", Desafiante, "perdedor competidor:", Competidor)
                        break
                    else:
                        print("A palavra no momento se encontra assim:", (segredo))
                        print(erros)
                        break
                time.sleep(3)
                os.system ("cls") 
            if resposta == 2:
                print(dica1)
                loop = 1
                time.sleep(3)
                os.system ("cls") 
            if resposta != 1 and resposta != 2:
                print ("resposta inválida")
                time.sleep(1)
                os.system ("cls") 
        if loop == 1:
            pergunta()
            resposta = int(input( ))
            if resposta == 1:
                print ("vamos la")
                time.sleep(1)
                os.system ("cls") 
                while True:
                    letra = str(input("digite uma letra: "))
                    if letra not in palavraChave:
                        erros = erros + (1)

                    if len in (letra) > "1":
                        print("mais de uma vez!")  
                
                    digitadas.append(letra)
                    
                    segredo = ""
                    for letra in palavraChave:
                        if letra in digitadas:
                            segredo += letra
                        else:
                            segredo += "*"
                        
                    if segredo == palavraChave:
                        print("Parabéns,", Competidor, "você ganhou!")
                        arquivo = open("registro.partida", "w")
                        arquivo.write("Palavra:", palavraChave, "vencedor competidor:", Competidor, "perdedor desafiante:", Desafiante)
                        break
                    if erros >= 5:
                        print("Vitória do desafiante! parabéns", Desafiante)
                        arquivo = open("registro.partida", "w")
                        arquivo.write("Palavra:", palavraChave, "vencedor desafiante:", Desafiante, "perdedor competidor:", Competidor)
                        break
                    else:
                        print("A palavra no momento se encontra assim:", (segredo))
                        print(erros)
                        break
                time.sleep(300)
                os.system ("cls") 
            if resposta == 2:
                print(dica2)
                loop = 2 
                time.sleep(3)
                os.system ("cls") 
            if resposta != 1 and resposta != 2:
                print ("resposta inválida")
                time.sleep(1)
                os.system ("cls") 
        if loop == 2:
            pergunta()
            resposta = int(input( ))
            if resposta == 1:
                print ("vamos la")
                time.sleep(1)
                os.system ("cls") 
                while True:
                    letra = str(input("digite uma letra: "))
                    if letra not in palavraChave:
                        erros = erros + (1)

                    if len in (letra) > "1":
                        print("mais de uma vez!")  
                
                    digitadas.append(letra)
                    
                    segredo = ""
                    for letra in palavraChave:
                        if letra in digitadas:
                            segredo += letra
                        else:
                            segredo += "*"
                        
                    if segredo == palavraChave:
                        print("Parabéns,", Competidor, "você ganhou!")
                        arquivo = open("registro.partida", "w")
                        arquivo.write("Palavra:", palavraChave, "vencedor competidor:", Competidor, "perdedor desafiante:", Desafiante)
                        break
                    if erros >= 5:
                        print("Vitória do desafiante! parabéns", Desafiante)
                        arquivo = open("registro.partida", "w")
                        arquivo.write("Palavra:", palavraChave, "vencedor desafiante:", Desafiante, "perdedor competidor:", Competidor)
                        break
                    else:
                        print("A palavra no momento se encontra assim:", (segredo))
                        print(erros)
                        break 
                time.sleep(3)
                os.system ("cls")   
            if resposta == 2:
                print(dica3)
                loop = 3
                time.sleep(3)
                os.system ("cls") 
            if resposta != 1 and resposta != 2:
                print ("resposta inválida")
                time.sleep(1)
                os.system ("cls") 
        if loop == 3:
            pergunta()
            resposta = int(input( ))
            if resposta == 1:
                print ("vamos la")
                time.sleep(1)
                os.system ("cls") 
                while True:
                    letra = str(input("digite uma letra: "))
                    if letra not in palavraChave:
                        erros = erros + (1)

                    if len in (letra) > "1":
                        print("mais de uma vez!")  
                
                    digitadas.append(letra)
                    
                    segredo = ""
                    for letra in palavraChave:
                        if letra in digitadas:
                            segredo += letra
                        else:
                            segredo += "*"
                        
                    if segredo == palavraChave:
                        print("Parabéns,", Competidor, "você ganhou!")
                        arquivo = open("registro.partida", "w")
                        arquivo.write("Palavra:", palavraChave, "vencedor competidor:", Competidor, "perdedor desafiante:", Desafiante)
                        break
                    if erros >= 5:
                        print("Vitória do desafiante! parabéns", Desafiante)
                        arquivo = open("registro.partida", "w")
                        arquivo.write("Palavra:", palavraChave, "vencedor desafiante:", Desafiante, "perdedor competidor:", Competidor)
                        break
                    else:
                        print("A palavra no momento se encontra assim:", (segredo))
                        print(erros)
                        break 
                time.sleep(3)
                os.system ("cls")   
            if resposta == 2:
                print("acabaram as dicas")
                loop = 3
                time.sleep(3)
                os.system ("cls") 
            if resposta != 1 and resposta != 2:
                print ("resposta inválida")
                time.sleep(1)
                os.system ("cls") 
    

