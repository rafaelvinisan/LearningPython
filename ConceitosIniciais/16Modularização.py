# Podemos criar os nossos próprios pacotes e módulos dentro de python
# aqui iremos importar o arquivo Contas.py, dentro de LearningPython e utilizar as funções do mesmo

from Pacote import Contas, func

print('Contas.soma(1,2,3,4) =', Contas.soma(1, 2, 3, 4))
print('Contas.multiplica(1,2,3,4) =', Contas.multiplica(1, 2, 3, 4))

# Usamos os modulos e pacotes para separar e organizar melhor nossos códigos
# todos pacotes devem conter um arquivo __init__.py

func() # a def func está dentro do arquivo __init__ e pode ser importada sem precisar chamar o arquivo em questão
