from time import sleep

def linha(tam=40):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(txt='cadastro.txt'):
    arquivo = open(txt, 'a')
    while True:
        c = {'v': '\033[32m', 'a': '\033[34m', 'f': '\033[m'}
        count = 1
        lista = ('Ver pessoas cadastradas', 'Cadrastrar nova Pessoa', 'Sair do Sistema')
        cabeçalho("MENU PRINCIPAL")
        for item in lista:
            print(f'{c["v"]}{count}{c["f"]} - {c["a"]}{item}{c["f"]}')
            count += 1
        linha()
        try:
            op = int(input(f'{c["v"]}Sua Opção:{c["f"]} '))
        except:
            print('\033[31mOpção invalida! Tente novamente!\033[m')
            continue
        if op == 1:
            extrato(arquivo.name)
        elif op == 2:
            cadastro(arquivo.name)
        elif op == 3:
            fechar(arquivo)
            break
        else:
            print('\033[31mERRO! Digite uma opção válida!\033[m')


def cadastro(txt):
    arquivo = open(txt, 'a')
    cabeçalho('NOVO CADASTRO')
    while True:
        nome = str(input('Nome: '))
        if nome.replace(' ', '').isalpha():
            break
        else:
            print('\033[31mNome invalido! tente novamente!\033[m')
    while True:
        try:
            idade = int(input('idade: '))
        except:
            print('\033[31mIdade invalido! tente novamente!\033[m')
        else:
            break
    linha = f'{nome:<30}{idade} anos\n'

    print(f'Novo registo de {nome} adicionado.')
    arquivo.write(linha)


def extrato(txt):
    cabeçalho('PESSOAS CADASTRADAS')
    arquivo = open(txt, 'r')
    print(arquivo.read())
    sleep(1)


def fechar(txt):
    sleep(0.5)
    cabeçalho("Saindo do sistem... Até logo!")
    sleep(0.5)
    txt.close()
