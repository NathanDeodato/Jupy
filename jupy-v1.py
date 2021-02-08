# Libs
from time import sleep
from DBJupy import BDJupy

# Colors
branco = '\033[1;97m'
cinza = '\033[1;90m'
vermelho = '\033[1;31m'
vermelho_claro = '\033[1;91m'
reset = '\033[0;0m'

# Start
print(cinza + "-=" * 79)
print(branco + "-- Jupy$ v1 --".center(158))
print(cinza + "-=" * 79)

sleep(1)

print(branco + "Óla! Me chamo Jupy.")
print("Fui criado, com o objetivo de responder ao usúario,")
print("ou seja, você. Perguntas as quais tenha a em meu BD(Banco de dados).")
print("Espero conseguir te ajudar.")

print(cinza + "-=" * 79)
sleep(1)

# Jupy
def Jupyv1():
    print(branco + "-- Jupy Types --".center(158))
    sleep(0.5)

    print("1 ° Jupy Comands °")
    sleep(0.5)

    print("2 ° Hardware °")
    sleep(0.5)

    print("3 ° Programming Language °")
    sleep(0.5)

    print("4 ° Console °")
    sleep(0.5)

    print(cinza + "-=" * 79)
    
    print(branco + "-- Jupy Start --".center(158))

    while True:
        try:
            type = int(input(branco + "Tipo: "))
            while type != 1 and type != 2 and type != 3 and type != 4:
                type = int(input(branco + "Tipo: "))
            
            sleep(1)

            question = str(input("Pergunta: ")).lower()#.replace(" ", "")
        except Exception as erro:
            print(cinza + "-=" * 79)
            print(vermelho_claro + "-- Jupy Error --".center(158))
            print(vermelho + f" Erro: {erro}" + reset)
            print(cinza + "-=" * 79)
        else:
            sleep(1)

            BDJupy(question, type)
            break


# First Start
Jupyv1()

# Jupy Loop
while True:
    try:
        print(branco + "-- Jupy Loop --".center(158))

        print("1 ° Sim °")
        print("2 ° Não °")

        go = int(input(branco + "Continue? "))
        while go != 1 and go != 2:
            go = int(input(branco + "Continue? "))

    except Exception as erro:
        print(cinza + "-=" * 79)
        print(vermelho_claro + "-- Jupy Error --".center(158))
        print(vermelho+ f" Erro: {erro}" + reset)
        print(cinza + "-=" * 79)
    else:
        print(cinza + "-=" * 79)

        if go == 1:
            Jupyv1()
        elif go == 2:
            print(branco + "--  Jupy Close --".center(158))
            print(cinza + "-=" * 79)
            break
