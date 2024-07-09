import random
import os

lista = []
lista_sorteados = []

while True:
    nome = input('Digite os nomes que serão sorteados: ')
    if nome != '':
        lista.append(nome)
    else:
        break



while True:
    if lista:
        os.system('cls')
        premiado = random.choice(lista)
        lista_sorteados.append(premiado)
       
        print(f'O premiado da vez é o {premiado}')

        opcao = input('Deseja realizar um novo sorteio? (s/n)').lower()
        os.system('cls')

        if opcao != 's':
            break
    else:
        print('Não existe nomes para serem sorteados!')
print('Sistema finalizado!')
print(lista)
print(lista_sorteados)