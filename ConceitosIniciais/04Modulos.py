import math # importando uma biblioteca
from time import sleep # importando uma função de uma biblioteca
from random import randint

n = 12.55
print(math.ceil(n)) # math.ceil faz o arredondamento de um numero para cima

sleep(5) # time.sleep(n) faz o código esperar n segundos antes de continuar, como somente essa função foi importada, pode ser chamada usando apenas o 'sleep'

print(randint(1,10)) # random.randint(x,y) gera um inteiro aleatório entre x e y