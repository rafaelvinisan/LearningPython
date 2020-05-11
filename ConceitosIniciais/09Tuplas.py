# As tuplas são uma das estruturas compostas em Python, estas são imutáveis e devem ser inicializadas entre parenteses

tupla1 = (1,'oi',True, 3.55, ' ^ ') # Uma tupla pode receber vários tipos
print(tupla1)
print(tupla1[0]) # é possivel acessar uma posição especifica da tupla
print(tupla1[0::2]) # Uma tupla pode ser fatiada assim como fazemos o fatiamento de strings
print(tupla1[-2]) # Mostra o valor na segunda posição contando do final para o início

for posicao, valor in enumerate(tupla1):
    print(f'posição {posicao+1} == {valor}')

sanduiche = ('pão', 'hamburger vegetariano', 'batata palha', 'queijo', 'picles', 'alface')
print(sorted(sanduiche)) # retorna os itens da tupla em ordem alfabética (como a tupla é imutável, o retorno é feito em
                            # forma de lista, e não de tupla

acompanhamentos = ('ketchup', 'suco de laranja', 'batata frita')

lancheCompleto = sanduiche + acompanhamentos # uma tupla pode ser formada da união de duas ou mais tuplas
print(lancheCompleto)