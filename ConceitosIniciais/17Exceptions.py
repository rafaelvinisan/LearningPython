# Para tratamento de erros em python é utilizado os comandos try e except
try:  # Irá testar o código abaixo
    numero = int(input('digite um inteiro: '))
except:  # Será executado em caso de erro (por exemplo se o numero informado não for um inteiro)
    print('Ocorreu um erro')
else:  # comando opcional que será executado caso não ocorra erros
    print('muito bem, voce digitou o numero {}'.format(numero))
finally:  # comando opcional que será executado independente de ocorrer erro ou não
    print('Fim do código')

# Podemos especificar o erro dentro do except
try:
    a = int(input('digite um valor para o numerador: ')) / int(input('digite um valor para o denominador: '))
except ZeroDivisionError:  # Erro dado caso tente executar uma divisão por 0
    print('o denominador não pode ser zero')
except TypeError:  # erro caso o tipo fornecido seja errado
    print('deve ser informado apenas digitos correspondentes a um numero inteiro')

# Também é possivel capturar uma exception para entrar em mais informações da mesma
try:
    a = int(input('digite um valor para o numerador: ')) / int(input('digite um valor para o denominador: '))
except Exception as erro:  # Captura a exception e salva na variavel erro
    print(erro)  # Mostra o nome do erro
    print(erro.__class__)  # Mostra a classe do erro

