"""
as operações existentes em python são:
+ adição
- subtração
// divisão inteira (para numeros inteiros)
% módulo (resto da divisão inteira)
/ divisão
* multiplicação
** potencia

"""

a = 8
b = 3

print(f'{a} + {b}  = {a+b}\n'
      f'{a} - {b}  = {a-b}\n'
      f'{a} // {b} = {a//b}\n'
      f'{a} % {b}  = {a%b}\n'
      f'{a} / {b}  = {(a/b):.2f}\n' # o comano :.2f formata o numero para ter apenas 2 casas decimais 
      f'{a} * {b}  = {a*b}\n'
      f'{a} ** {b} = {a**b}\n')

# para substituir uma variavel pelo resultado de uma operação feita com ela mesmo, podemos utilizar a sintaxe a seguir

a = a+1 # a recebe a + 1
print(a)

a += 1 # a recebe o acrécimo de 1
print(a)