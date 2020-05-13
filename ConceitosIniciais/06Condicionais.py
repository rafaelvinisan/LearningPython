# Para usar um condicional em Python, não utilizamos parenteses para indicar qual a condição e nem chaves para o bloco
# de comandos a ser executado. Os comandos executados seguirão a identação do seu código, por isso é importante mais do
# que nunca se atentar para a organização do mesmo.

idade = int(input('quantos anos você tem? '))

if idade >= 18:  # ao fim da condição usa-se :
    print('maior de idade')
else:
    print('menor de idade')

# existe em Python o condicional 'elif' (concatenação de else + if) para evitar que você precise digitar um else segido de if:

if 0 < idade < 12:
    print('criança')
elif 12 <= idade < 18:
    print('adolecente')
elif 18 <= idade < 25:
    print('jovem')
else:
    print('adulto')

# qualquer trecho de código que retorne um boolean, pode ser usado como condição do seu if.

nome = str(input("insira seu nome: ")).strip()

if 'a' in nome.lower():
    print('seu nome possui a letra a')
else:
    print('seu nome não possui a letra a')

# podemos também incluir uma condicional dentro da função print

print("seu nome é curto" if len(nome) < 4 else "seu nome não é curto")

# para adicionar uma nova condição ao seu if ou elif, utiliza-se 'and' para 'e' e 'or' para 'ou'

if nome.endswith('a') and len(nome) > 3:  # o método endswith retorna True se a string terminar com o caractere
                                              # passado por parametro
    print('Seu nome termina com a letra A, mas você não se chama Ana')

elif nome.endswith('o') or nome.endswith('l') or nome.endswith('e'):

    print('seu nome termina com o, l ou e')

else:

    print('que belo nome!')
