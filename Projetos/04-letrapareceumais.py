import os
os.system("CLS")
print("="*25," ( Contagem de Letras ) ","="*25,end="\n\n")

frase = input("Digite uma frase: ")
os.system("CLS")
print("="*15," ( Contagem de Letras ) ","="*15,end="\n\n")
print(f'"{frase}"')

contador = 0
letra_que_apareceu_mais = ""
quanto_apareceu_mais = 0

while contador < len(frase):
    letra_atual = frase[contador]

    if letra_atual == " ":
        contador+=1
        continue
 
    quanto_apareceu_mais_atual = frase.count(letra_atual)

    if quanto_apareceu_mais < quanto_apareceu_mais_atual:
        quanto_apareceu_mais = quanto_apareceu_mais_atual
        letra_que_apareceu_mais = letra_atual
    
    contador+=1

print(f"\nLetra que apareceu mais: {letra_que_apareceu_mais}")
print(f"Quantas vezes {letra_que_apareceu_mais} apareceu: {quanto_apareceu_mais}")