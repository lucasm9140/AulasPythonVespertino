import time
lista = []

while True:
    if lista:
        contador = 0
        print('Enquanto houver algo dentro da lista você verá essa mensagem\n')
        time.sleep(5)
        print('Vamos ver o que tem dentro da lista:\n')
        time.sleep(5)

        for i in lista:
            print(f'Elemento na lista: {i}')
            time.sleep(5)
            contador += 1
            print(f'Quantidade de acessos à lista: {contador}')

        opcao = input('Deseja adicionar mais um item à lista? (s - sim, n - não): ').lower()

        if opcao == 's':
            novo_item_lista = input('\nDigite o que você quer adicionar na lista: ').lower()
            time.sleep(5)
            lista.append(novo_item_lista)
            print('\nItem adicionado à lista!')
        else:
            print('\nVocê escolheu não adicionar mais itens à lista. Saindo do loop.')
            break

    else:
        print('A lista está vazia.\n')
        time.sleep(5)
        print('Vamos adicionar alguns itens à lista para continuar.\n')

        while True:
            novo_item_lista = input('Digite o que você quer adicionar na lista: ').lower()
            time.sleep(5)
            lista.append(novo_item_lista)
            print('\nItem adicionado à lista!')
            time.sleep(5)

            opcao = input('Deseja adicionar mais um item à lista? (s - sim, n - não): \n').lower()

            if opcao != 's':
                time.sleep(5)
                print('Você escolheu não adicionar mais itens à lista. Saindo do loop inicial.')
                break
time.sleep(5)
print('Saindo do programa. Você está fora do loop. Caso queira criar mais coisas e outros loops, comece a partir desse ponto')

