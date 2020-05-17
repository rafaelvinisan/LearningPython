# As listas são variaveis compostas mutaveis e ordenadas, ou seja, podemos modificar e acessar posições exatas
# as listas são denotadas por colchetes

lista = []  # Pode ser inicializada, vazia, assim
lista1 = list()  # mas também podemos inicializar uma lista vazia desta maneira
lista2 = ['Padrinhos mágicos', 'Tres espiãs demais', 'As aventuras de Jackie Chan']
print('lista2 = ', lista2)

# por ser ordenada, podemos fatiar uma lista

print('lista2[0] = ', lista2[0])
print('lista2[::2] = ', lista2[::2])

# é possivel trocar um ou mais valores de uma lista

lista2[2] = 'As Aventuras de Julie Perlin'
print('lista2 = ', lista2)

# Para adicionar elementos em uma lista usa-se os métodos insert() ou append()
# o append irá adicionar elementos na ultima posição da lista

lista2.append('Coragem o cão covarde')
lista2.append('Caverna do dragão')
print('lista2 = ', lista2)

# com o metodo insert podemos inserir um valor em uma posição especificada, reorganizando a lista

lista2.insert(1, 'Bob esponja') # o novo valor será adicionado entre os elemenntos de posição 0 e 1
print('lista2 = ', lista2)

# para remover valores de uma lista podemos usar a função del ou os metodos pop e remove

del lista2[0] # deleta o elemento na posição 0
print('lista2 = ', lista2)
lista2.pop(0) # dleta o elemento na posição 0, entretanto se o pop não receber parametros, deleta o ultimo elemento
lista2.pop()
print('lista2 = ', lista2)
lista2.remove('Tres espiãs demais') # no método remove, passamos por parametro o valor a ser removido, e não seu indice
print('lista2 = ', lista2)

# para passar uma lista como valor sem que crie uma ligação com a nova variavel asim como acontece com os conjuntos, podemos fazer de duas formas

lista2equal = lista2 # qualquer alteração em uma variavel ira alterar a outra
lista2copy = lista2.copy() # método copy
lista2fat = lista2[:] # passando um fatiamento da lista
lista2copy.append('Steven Universe') # irá alterar apenas a lista2copy
lista2fat.pop() # ira alterar apenas a lista2fat
lista2equal.append('Irmão do Jorel') # irá alterar a lista2equal e lista2
print('lista2 = ', lista2)
print('lista2equal = ', lista2equal)
print('lista2copy = ', lista2copy)
print('lista2fat = ', lista2fat)

# a função len pode ser usada para saber o tamanho tambem de estruturas compostas

print('len(lista2) = ', len(lista2))