# Exercicio - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta' : 'Quanto é 2+2?',
        'Opções' : ['1', '3', '4', '5'],
        'Resposta' : '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta':'5',
    },

]

act = 0

for i in perguntas:

    print(f'Pergunta: {i["Pergunta"]}\n')
    print('Opções:')

    for pos, valor in enumerate(i['Opções']):
        print(f'{pos}) {valor}')
    resp = input('Escolha uma opção: ')

    try:
        if i['Opções'][int(resp)] == i['Resposta']:
            act += 1
            print('Acertou\n')
        else:
            print('Errou\n')
    except:
        print('Errou\n')

print(f'Você acertou {act} de {len(perguntas)} perguntas')