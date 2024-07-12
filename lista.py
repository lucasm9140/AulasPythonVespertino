lista_nomes = ['Fulano', 'Cicrano', 'Beltrano', 'Pedro', 'Lucas', 'Gomes', 'Eulete']

# Lista original
for i in range(len(lista_nomes)):
    print(f'{i + 1}° nome da lista é: {lista_nomes[i]}')

novo_nome = input('Digite o novo nome que sera adicionado na lista: ')

posicao = input('Digite a posição que deseja colocar esse nome: ')
posicao = int(posicao)

# Corrigindo a posição
posicao -= 1

if posicao >= 0 and posicao <= len(lista_nomes):
    lista_nomes.insert(posicao, novo_nome)
else:
    print('Posição inválida!')

# exiba a lista atualizada
print()
print(30*'=', 'Lista Atualizada', 30*'=')

for i in range(len(lista_nomes)):
    print(f'{i + 1}° nome da lista é: {lista_nomes[i]}')