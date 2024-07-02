"""

Nesse programa, o usuário vai receber algumas instruções antes de começar o jogo de adivinhar a palavra secreta.
As instruções são:  Digitar "stop" para sair do jogo e "cls" para limpar a tela.
Fiz um pequeno sistema para verificar se ele digitou de fato uma letra, não um número, ou várias letras. 
Conforme o usuário acerta as letras, a palavra que antes estava oculta (*******), começa a aparecer (s**u**t*).
Ao final, é exibido quantas tentativas o usuário fez.

"""
import os 
os.system("cls")

print("="*16," ( Jogo - Advinhe a Palavra ) ","="*16,end="\n\n")
print('Digite\n"stop" para sair do jogo ou\n"cls" para limpar a tela\n')
os.system("PAUSE")

os.system("CLS")
PALAVRA_SECRETA = "Security"
tamanho_da_palavra = len(PALAVRA_SECRETA)
contador =0
letras_acertadas = ""

letra = ""

while letra != "stop":
    letra = input("Digite uma letra: ")
    try:
        var_teste = int(letra)
        if(type(var_teste) == int):
            print("Você digitou um número não uma letra! ")
            continue
    except:
        if(letra.lower() =="cls"):
            os.system("CLS")

        elif(letra.lower() == "stop"):
            break

        elif(len(letra)>1):
            print("Digite apenas uma letra")
            continue 
        
        elif(len(letra)==0):
            print("Você não digitou uma letra! ")
            continue
        
        contador +=1 

        if(letra in PALAVRA_SECRETA):
            letras_acertadas += letra
        
        palavra_formada = ""
        for letra_secreta in PALAVRA_SECRETA:
            if letra_secreta in letras_acertadas:
                palavra_formada +=letra_secreta
            else:
                palavra_formada+="*"
        
        print("Palavra Secreta: ",palavra_formada)

        if(palavra_formada == PALAVRA_SECRETA):
            print("VOCÊ GANHOU!!!")
            print("A palavra era: ", PALAVRA_SECRETA)
            print("Tentativas: ",contador)
            contador =0
            letras_acertadas = ""
