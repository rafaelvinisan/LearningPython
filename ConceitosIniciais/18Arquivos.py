nome_do_arquivo = str(input('insira o nome do arquivo: '))

criar = open(nome_do_arquivo, 'w+')  # o comando open irá abrir o arquivo especificado e o 'w' (write) denota que será para escrita
                                     # o + serve para criar um arquivo com o nome especificado caso o mesmo ainda não exita
criar.writelines('criado com sucesso\n')  # escreve no arquivo
criar.close()  # fecha o arquivo

# o parametro 'w' possibilita que você escreva no arquivo com o metodo write, entretanto esta escrita irá apagar tudo que ja existia no arquivo anteriormente
# para poder adicionar escritas sem apagar os dados que já existiam no arquivo, usa-se o parametro 'a' (append)
escrever = open(nome_do_arquivo, 'a')
escrever.write(input('escreva algo no arquivo: '))  # Um texto é sempre escrito logo após o fim do texto anterior, por isso
                                                    # é importante quebrar linhas ou espaçar após uma nova inserção
escrever.write('\n')

# podemos também passar uma lista por parametro de escrita com o método writelines
list = ['-' * 30 + '\n',
        'linha acima'.center(30) + '\n',
        'linha do meio'.center(30) + '\n',
        'linha abaixo'.center(30) + '\n',
        '-' * 30
        ]
escrever.writelines(list)
escrever.close()

leitura = open(nome_do_arquivo, 'r')  # o parametro 'r' abre o arquivo para leitura
print(leitura.read())
print(leitura.read())  # se tentarmos executar a leitura novamente, o retorno será uma string vazia
# Isso ocorre pois o arquivo já foi inteiro lido, e para ser relido devemos fechar e abrir para leitura novamente
leitura.close()
print('segunda leitura:')
leitura = open(nome_do_arquivo, 'r')
leitura.read()
