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