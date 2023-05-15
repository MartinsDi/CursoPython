# 115 - Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções cadastrar uma nova pessoa e listar todas as pessoas cadastradas.


'''from Exercicios.Ex115.cadastro import menu
menu('Cadastro.txt')'''


from Exercicios.Ex115.lib.interface import *



while True:
    resposta = menu(['Ver pessoa cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        print('Hello world')
    elif resposta == 2:
        print()
    elif resposta == 3:
        print()
    else:
        print('LIXO')


