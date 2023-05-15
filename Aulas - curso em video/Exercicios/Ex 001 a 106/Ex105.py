# 105 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função
def notas(*n, sit=False): # Versãos do professor
    """
    → Função pra analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit:valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


'''def notas(*n, sit=False):
    """
    → Função pra analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit:valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    notas = dict()
    maior = menor = media = 0
    for i in n:
        if i > maior:
            maior = i
        if i < menor or menor == 0:
            menor = i
        media += i
    media = media / len(n)
    notas['maior'] = maior
    notas['menor'] = menor
    notas['media'] = media
    if sit:
        if media >= 7:
            notas['situação'] = 'BOA'
        elif media >= 5:
            notas['situação'] = 'RAZOÁVEL'
        else:
            notas['situação'] = 'RUIM'
    return notas'''


resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
