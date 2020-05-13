"""os tipos primitivos existentes em Python são:

int = número inteiro. ex: (-1,0,1,2,3,4,5...)
float = número com ponto flutuante(reais). ex (1.5 , -5.87568 , 0,1415...)
bool = valores lógicos (True, False)
str = conjunto de caracteres. ex: ('oi', '12345', '')

"""

# O Python não exige que suas variaveis sejam tipadas, entretando elas devem ou serem tipadas, ou inicializadas

v1 = int  # como n1 foi tipada, não precisa ser inicializada
v1 = 0
print(f'n1 = {v1}')

v2 = int(input('digite um numero: '))  # n2 foi tipada e será inicializada pelo usuário
print('n2 =', v2)

v3 = input('digite algo: ')  # n3 será inicializada pelo usuário e pode receber qualquer tipo
print(f'n3 = {v3}')

v4: str = 'aeiou'  # o tipo da variavel pode ser explicitado utilizando a sintaxe "_nome da var_ : _tipo_ = _valor_"
print('v4 = ' + v4)

# uma variavel pode mudar de tipo no meio do programa
v1 = 'assistam carros 2'
print(f'novo valor de v1 = "{v1}"')
