# Podemos documentar uma função utilizando tres aspas duplas


def aniversario(id: int, aniv=1):
    """
    a def aniversario recebe a idade de uma pessoa e retorna esta atualizada após n aniversários
    por padrão o numero de aniversários é 1, mas isso pode ser alterado conforme a necessidade

    :param id: idade original da pessoa (int)
    :param aniv: quantos anos devem ser acressidos? (se não especificado será 1)
    :return: id + aniv (int)
    """

    return id + aniv


help(aniversario)  # Usando a função help, é possivel ver a documentação de qualquer função, tipo ou método de python
