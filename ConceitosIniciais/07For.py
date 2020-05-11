# No exemplo a seguir, para utilizaro o comando for, será criado uma variavel c que irá receber valores
# dentro do intervalo de 1 até 11 (parando no 10), e para cada valor ela será printada na tela

print('contando de 0 a 10:')
for c in range (0,11):
    print(c, end=(', ' if c != 10 else '.\n') ) # printa o numero c na tela e caso ele seja diferente de 10 adiciona ', ' antes de printar o próximo
                                            # caso seja 10 irá saltar uma linha

print('numeros pares de 0 a 10')
for c in range(0,11,2): # esse numero 2 adicionado fará com que o programa conte de 2 em 2 números
    print(c, end=(', ' if c != 10 else '.\n'))

print('contagem decrescente 10 a 0')
for c in range (10,-1,-1):
    print(c, end=(', ' if c != 0 else '.\n'))

print("somando 5 numeros fornecidos pelo usuário:")
soma = 0
for c in range (0,5):
    soma += int(input("insira um inteiro: "))
    print(f'apenas 1 valor fornecido, seu valor é: {soma}' if (c+1) == 1 else f'{c+1} valores fornecidos, a soma deles '
    
                                                                              f'é igual a {soma}')
palavra = 'bola'
print("letras da palavra")
for posicao, letra in enumerate(palavra): # o for de uma string retorna cada caractere da mesma, o enumerate torna possivel vc saber
                                            # qual a posição deste caractere, como no exemplo a seguir
    print(f'o {posicao+1}º caractere é: {letra}')
