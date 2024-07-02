"""
Aqui temos uma calculadora bem simples em Python, 
minha ideia foi usar "linhas de comando" para fazer as operações ao invés de simbolos tradicionais(+,-,*,/),
(como o "cls","ipconfig","color" ... do CMD do Windows.
"""
import os

new="s"
while(new!="n"):
    os.system("CLS")

    print("="*20,"( Calculadora )","="*20,end="\n\n")
    print('"som" -> Soma\n"sub" -> Subtração\n"mul" -> Multiplicação\n"div" -> Divisão\n"exp" -> Exponênciação\n"por" -> Porcentagem\n')

    opc = str(input("\n\nDigite a opção desejada: "))
    os.system("CLS")

    print("="*20,"( Calculadora )","="*20,end="\n\n")
    operacao = 0
    exope = 0
    if(opc == "som"):
        exope = "+"
    elif(opc =="sub"):
        exope = "-"
    elif(opc =="mul"):
        exope = "*"
    elif(opc =="div"):
        exope = "/"
    elif(opc =="exp"):
        exope = "**"
    else:
        exope="%"
    print(f"[Operação em Uso]--> {exope}")

    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("\nDigite o segundo número: "))

    resultado = 0

    if(opc == "som"):
        resultado=num1+num2
    elif(opc =="sub"):
        resultado=num1-num2
    elif(opc =="mul"):
        resultado=num1*num2
    elif(opc =="div"):
        resultado=num1/num2
    elif(opc =="exp"):
        resultado=num1**num2
    else:
        resultado=(num1*num2)/100

    os.system("CLS")
    print("="*20,"( Calculadora )","="*20,end="\n\n")
    print(f"{num1} {exope} {num2} = {resultado:.3f}")
    new=str(input("Deseja fazer uma nova operação (s/n) ?\n"))
