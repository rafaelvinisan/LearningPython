# O conjunto (ou set) é uma estrutura composta não ordenada, ou seja, não há como saber qual a ordem das variaveis dentro de um conjunto
# Os conjuntos são denotador por chaves mas podem ser criados como 'set()'

c1 = set() # cria um conjunto vazio
c2 = {'oi', 'tudo', 'bem', 'com', 'voce', '?'}
print('c2 = ', c2)

# Os elementos de um set não podem ser alterados, mas podem ser adicionados
# Usamos o método add para adicionar um valor a um conjunto

c1.add('primeiro add')
c1.add('segundo add')
print('c1 = ',c1)

# O add só aceita uma variavel simples, para passar por parametro variaveis compostas usamos o update
# Podemos passar mais de um valor por parametro pelo método update, entretanto este valor deve ser uma variavel composta (incluindo str) ou um char
c1.update(c2)
print('c1 = ',c1)

# podemos unir dois conjuntos com o metodo union

c3 = {'usando', 'union'}
c2 = c2.union(c3)
print('c2 = ',c2)

# Para remover um elemento pode-se usar os métodos: remove, discard e pop
# O método remove gera um erro caso o elemento especificado para ser removido não exista

c1.discard('segundo add')
c1.remove('primeiro add')
print('c1 = ',c1)

# o pop remove o ultimo elemento, porem como sets não são ordenados, o elemento removido será aleatório
c1.pop()
print('c1 = ',c1) # cada vez que o programa for rodado, o valor retirado será escolhido aleatóriamente novamente

# o clear pode ser usado para apagar um set inteiro
c1.clear()
print('c1 = ',c1)

# quando criamos uma relação de igualdade com uma variavel composta, qualquer alteração feita em uma variavel, modificará as duas
cigual3 = c3 # A variavel cigual3 recebe c3
cigual3.add(2) # apenas a variavel cigual3 está recebendo o acressimo de valor
print('c3 = ',c3) # entretando podemos ver que a variavel c3 também será alterada

# Para evitar isso, devemos passar uma cópia do set para a nova variavel
c3copy = c3.copy()
c3copy.remove(2)
print('c3copy = ', c3copy)
print('c3 = ',c3)

