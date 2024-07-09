import random

numero_secreto = random.randint(1,20)

tentativas = 0
max_tentativas = 5
acertou = False

print('Bem-Vindo ao Python Games!')
print(f'Você possui {max_tentativas} tentativas para adivinhar o numero secreto entre 1 e 20')

while tentativas < max_tentativas:
    palpite = int(input('Digite um numero inteiro: '))
    #print(f'Numero secreto: {numero_secreto}')
    tentativas +=1
    #print(f'Número de tentativas: {tentativas}')

    if palpite == numero_secreto:
        acertou = True
        break
    elif palpite < numero_secreto:
        print('Tente um numero maior!')
    else:
        print('Tente um numero menor!')

if acertou:
    print(f'Parabéns! Voce acertou o  número secreto {numero_secreto} em {tentativas} tentativas.')
else:
    print(f'Que pena! Você não conseguiu adivinhar o número secreto {numero_secreto}')