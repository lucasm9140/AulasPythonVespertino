import os
import time

cont = int(input("Digite um numero inteiro: "))

while cont >= 0:
    os.system('cls')
    print(f'Contagem regressiva: {cont}...')
    time.sleep(1)
    cont -=1

os.system('cls')
print('BOOOOOOOOOOOOOMMMMMMMMMMM!!!!')