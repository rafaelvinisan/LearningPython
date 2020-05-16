# Os dicionários são estruturas compostas que ao inves de indices, possuem uma key, esta formada por uma string

dicionario = dict() # Inicializando um dicionario vazio
dicionario1 = {} # Inicializando dicionario vazio
dados = {'Nome': 'Maria Eugênia', 'Idade': 25} # Os dados dentro deste dicionario possuem keys para serem acessados (Nome e Idade)
print('dados = ', dados)
print('dados["Nome"] = ', dados['Nome']) # Acessa a informação referente à key Nome
print('dados["Idade"] = ', dados['Idade']) # Acessa a informação reefrente à key Idade

# Para adicionar um novo valor, apenas referenciamos a nova key e inserimos o valor

dados['Profissão'] = 'Marceneira'
print('dados = ', dados)

# Para editar algum valor, apenas referenciamos uma key já existente

dados['Idade'] = 26
print('dados["Idade"] = ', dados['Idade'])

# Para deletar elementos, deve-se usar o comando del

del dados['Idade']
print('dados = ', dados)

print('dados.values() = ', dados.values()) # O método values retorna apenas os valores dentro do dict
print('dados.keys() = ', dados.keys()) # O método keys retorna apenas as keys
print('dados.items() = ', dados.items()) # Items retorna os pares(key, value)

for chave, valor in dados.items():
    print(f'key = {chave}; valor = {valor}')