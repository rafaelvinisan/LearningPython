# Para definir uma função em ython, usa-se a palavra reservada 'def'


def newyear():
    print('Firmeza total, mais um ano se passando')


newyear()


# Uma função pode receber parametros sem especificar seu tipo


def oi(nome):
    print(f'Suavidade demais {nome}?')


parametro_def_1 = str(input('Qual é seu nome? '))  # recebe um nome passado pelo usuário
oi(parametro_def_1)  # Passa o nome recebido por parametro

# Podemos inserir o input na passagem de parametro

oi(str(input('digite outro nome: ')))

# Para uma função com mais de um parametro, podemos na passagem dos mesmos explicitar a ordem


def subtrai(x1, x2):
    print(f'{x1} - {x2} = {x1 - x2}')


subtrai(x2=5,
        x1=10)  # desta maneira o primeiro valor passado foi para o x2, e não para o x1 como aconteceria sem explicitar


# Podemos também definir valores padrões para algum parametro, que serão utilizados caso o mesmo não seja especificado


def metido(nome,
           metido=True):  # desta maneira, especificamos que a variavel falso recevera o valor booleano 'True' por padrão
    if metido:
        print(f'o {nome} é muito metido')
    else:
        print(f'o {nome} não é metido, só falso')


metido('Janderson')  # passamos apenas o arametro nome, logo o parametro 'metido' receberá valor True
metido('Percyjacksonsvaldo', False)  # Modificamos o parametro 'metido' para receber valor False


# Quando precisamos que uma função receba uma quantidade desconhecida de parametros, podemos usar o conceito de empacotamento


def soma(*valores):  # usando o * criamos uma tupla que pode receber n valores
    total: int = 0
    for c in valores:
        total += c
    print(f'a soma de todos valores é igual a {total}')


soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
soma(3, 2, -1)

# Uma função pode retornar algum valor, e o tipo do retorno não precisa ser especificado

def multiplica (*valores):
    total: int = 1
    for c in valores:
        total *= c

    return total # A função irá retornar o total (tipo int)


print(multiplica(1,2,3,4,5))