# O comado while não inicializa uma variavel automáticamente

contador = 0
print('contando de 0 a 10 com while')
while contador <= 10:
    print(contador, end=(', ' if contador != 10 else '.\n'))
    contador += 1

# Usando 'True' como condição do while, podemos criar um loop infinito

parada: int
while True: # O loop irá ocorrer até que exista um break
    parada = int(input('digite um valor (0 para sair do loop infinito): ')) # 'parada' recebe valor fornecido pelo usuario
    if parada == 0:
        break  # O break é usado para quebrar um loop, neste caso será ativado após o usuário informar um valor igual a 0
print('saí do loop')

# Usando o while para validar uma resposta

resp: str
while True:
    resp = str(input('responda sim ou não [S/N]: ')).strip().lower()
    if len(resp) != 1 or resp not in 'sn':
        print('ERRO!! insira uma resposta válida [S/N]')
    elif resp == 's':
        print('sua resposta foi Sim!!')
        break
    elif resp == 'n':
        print('sua resposta foi: Não...')
        break

# Calculando fatorial com while

fat = 1
n = int(input('deseja saber o fatorial de qual numero? '))
while n > 1:
    fat *= n
    n -=1
print(f'fatorial igual a {fat}')
