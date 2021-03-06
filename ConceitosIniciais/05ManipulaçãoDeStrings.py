# Uma String é uma sequencia de caracteres sendo que o primeiro caractere ocupa a posição 0 da String

# Alinhamento:
s1 = 'ola Python'
print(f'{s1:>20}')  # o ':>20', alinha a string a direita dentro de 20 espaços
print(f'{s1:^15}')  # usando o :^15 o texto será alinhado ao centro em 15 espaços
print(f'{s1:<}')  # com o > o alinhamento é feito normalmente, à esquerda
# O alihamento pode ser feito usando os métodos center, ljust e rjust também

# Repetição
print('-'*30) # o caractere - será printado 30 vezes na tela
print('repetição'.center(30))
print('-'*30)

# Fatiamento:
print(s1[0])  # mostra o caractere da posição 0

# podemos fatiar uma string usando dentro do colchete [mostrar dessa posição : até a posição anterior a esta]

print(s1[2:8])  # mostra os caractere da posição 2 até a posição 7

print(s1[:4])  # quando o primeiro valor não é especificado, o fatiamento começa na posição 0
print(s1[4:])  # quando o segundo valor não é especificado, o fatiamento vai até o final da string

# quando apresentamos um terceiro valor s1[inicio:fim:n], a string será fatiada de n em n caracteres:
print(s1[1:10:2])  # mostra os caracteres da posição 1 até a 10 saltando de 2 em 2 (1,3,5,7,9)

# alguns Métodos e Funções

print(f'len(s1): {len(s1)}\n'  # a função len retorna o numero de caracteres na string
      f's1.count("o"): {s1.count("o")}\n'  # retorna quantas vezes o caractere (no caso o 'o') aparece na string
      f's1.find("Pyt"): {s1.find("Pyt")}\n'  # retorna a posição em que o caractere ou a sequencia de caracteres começa pela primeira vez
      f's1.find("oloquinho meu"): {s1.find("oloquinho meu")}\n'  # caso o caractere ou sequencia não exista na string, retorna -1
      f'"ola" in s1: {"ola" in s1}\n'  # retorna um boolean indicando se existe ou não os caracteres na string
      f's1 in "meus amigos, ola Pythoncrazy": {s1 in "meus amigos, ola Pythoncrazy"}\n'  # retorna um boolean indicando se existe ou não a string indicada na sequencia de caracteres fornecida
      f's1.replace("ola", "colé"): {s1.replace("ola", "colé")}\n'  # Substitui uma sequencia de caracteres por outra
      f's1.upper: {s1.upper()}\n'  # Coloca toda String em maiusculo
      f's1.lower: {s1.lower()}\n'  # Todas letras em minusculo
      f's1.capitalize: {s1.capitalize()}\n'  # Apenas primeiro caractere maiusculo
      f's1.title: {s1.title()}\n'  # faz o capitlize em cada palavra da string
      )

s2 = "   super fantastico amigo    "
print(f's2 == {s2}')
print(f's2.strip(): {s2.strip()}')  # remove os espaços antes e depois da string
print(
    f's2.split: {s2.split()}')  # separa a string por palavras, por padrão o split quebra a string quando encontra um ' ', entretando o caractere pode ser especificado passado por parâmetro
print(
    f's2.split("a"): {s2.split("a")}')  # Neste caso as strings foram separadas sempre que encontrasse um caractere 'a'
