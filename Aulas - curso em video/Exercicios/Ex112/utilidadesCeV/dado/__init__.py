'''def leiaDinheiro(msg):
    while True:
        num = str(input(msg)).strip().replace(',','.')
        numero = False
        if i.isalpha():
            print(f'\033[31mErro: \"{num}\" é um preço inválido!\033[m')
        else:
            for i in num:
                if i.isnumeric():
                    numero = True
                else:
                    if i in ',':
                        vir = True
                        break
            if numero:
                n = float(num)
                break
            else:
                print(f'\033[31mErro: \"{num}\" é um preço inválido!\033[m')

    return n'''

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().replace(',','.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mErro: \"{entrada}\" é um preço inválido!\033[m')
        else:
            return float(entrada)