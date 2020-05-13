# o comando print escreve na tela, por convenção o texto dentro do print fica entre aspas simples
# entretanto também funciona com aspas duplas
print('hello World')
print("ola Mundo")

# O comando print, salta uma linha ao seu fim automaticamente, entretando podemos definir um "final alternativo" para
# ser executado ao fim, utilizando o ", end='' ", onde o texto dentro das aspas simples será mostrado ao fim do comando
# print ao inves de saltar linha

print('na mesma', end=' ')
print('linha')

# Para receber dados do usuário o comando utilizado é o "input()", este dado deve ser armazenado em alguma variavel criada
# que não precisa necessáriamente receber um tipo. o comando input() pode receber uma string como parametro, essa será mostrada ao usuário
# antes que ele insira o dado

nome = input('digite um nome: ') # o nome digitado será armazenado na variavel "nome", note que a variavel nome não foi tipada, logo pode receber qualquer tipo de dado
idade: int = int(input('qual a sua idade?\n')) # a variavel idade é, obrigatóriamente, um numero inteiro

# dados dentro de um print() podem ser concatenados de 3 maneiras diferentes apresentadas a seguir

print('ola' + nome) # utilizando um + é possivel concatenar 2 strings
print('você tem', idade, 'anos') # com a , podemos concatenar quaisquer tipos de dados

# quando é preciso várias concatenações, o ideal é utilizar o método .format(), com ela utilizamos dentro da string o sinal
# de {}, que será substituido ao final pelo dado desejado, inserido dentro do .format() em ordem de aparição

print('ola {} você tem {} anos'.format(nome, idade))

# outra maneira de usar o print formatado é digitando um f antes de abrir as aspas simples. Isso permite que dentro das
# chaves{} você já insira o dado que deseja que apareça naquela posição, eliminando a necessidade de usar o .format() ao final

print(f'o {nome} possui {idade} anos de idade')