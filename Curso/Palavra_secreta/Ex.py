from random import choice

lista = ['Cravo', 'Bambu', 'Galinha', 'Língua', 'Cachimbo', 'Barco', 'Girafa', 'Banjo', 'Bolsa', 'Elefante', 'Girassol',
        'Guitarra', 'Cogumelo', 'Canguru', 'Caminhão']


palavras = [list(choice(lista).lower()),list, list('')]
palavras[1] = list('_' * len(palavras[0]))
num = [1,0]

while True:
    print(f'Tentativa {num[0]}')
    let = input('Adivinhe uma letra: ')[0].lower()
    if not let.isalpha():
        print('Não é uma letra, tente novamente!')
        continue
    num[0] +=1
    if let not in palavras[0]:
        if let not in palavras[2]:
            palavras[2].append(let)
            #palavras[2] += f'{let} '
        print(palavras[2])
        continue
    elif let in palavras[0] and let not in palavras[1]:
        num[1] += palavras[0].count(let)
        if palavras[0].count(let) == 0:
            palavras[1][palavras[0].index(let)] = let
        else:
            for j, i in enumerate(palavras[0]):
                if i == let:
                    palavras[1][j] = let
    print(palavras[1])
    if num[1] == len(palavras[0]):
        print('Você acertou!')
        break