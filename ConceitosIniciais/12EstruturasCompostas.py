# Podem existir variavéis que são estruturas compostas, dentro de estruturas compostas
# como por ex: listas de listas, listas de tuplas, tuplas de conjuntos e etc
# estas estruturas seriam como correspodentes a 'matrizes'

a2 = (4,5,6)
a = ({'um', 'dois', 'tres'}, a2, [7, 8, 9])

print('a variavel "a" possui na:')
for index, tipo in enumerate(a):
    print(f'{index+1}ª posição um(a) {type(tipo)}')

atletas = [['Josias', 'Rugby'], ['Raimunda', 'Cricket'], ['Geraldete', 'Futebol Gaélico']] # Lista de listas
print('atletas = ', atletas)
print('atletas[1] = ', atletas[1]) # mostra a variavel na posição 1, no caso é uma lista
print('atletas[1][0] = ', atletas[1][0]) # mostra a variavel na posição 0 dentro da lista que está na posição 1 de atletas

for c in atletas:
    print(c[1]) # irá printar todos os esportes

print('atletas[2]:')
for c in atletas[2]: # a variavel c irá percorrer a variavel dentro da posição 2 de atletas
    print(c)