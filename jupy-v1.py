# Libs
from time import sleep
from DBJupy import BDJupy

# Colors
branco = '\033[1;97m'
cinza = '\033[1;90m'
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
sleep(2)

print(branco + "-- Jupy Types --".center(158))
sleep(0.5)

print("1° Jupy Comands °")
sleep(0.5)

print("2° Hardware °")
sleep(0.5)

print("3° Programming Language °")
sleep(0.5)

print("4° Console °" + reset)
sleep(0.5)

print(cinza + "-=" * 79)


# Jupy
def Jupyv1():
    type = int(input(branco + "Tipo: "))
    
    sleep(1)

    question = str(input("Pergunta: ")).lower()

    sleep(1)

    BDJupy(question, type)


Jupyv1()
