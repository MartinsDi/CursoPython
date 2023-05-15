# 70 - Crie um program que leia o nome e o preço de varios produtos. o programa devera perguntar se o usuario vau continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

total = qtdMil = vlrMenor = 0
nomeMenor = ''
print("-"*30)
print(f'{"LOJA SUPER MANNY":^30}')
print("-"*30)
while True:
    nome = str(input('Nome do produto: ')).strip().title()
    preco = float(input("Preço: R$ "))
    total += preco
    if vlrMenor == 0: #or preco < vlrMenor / isso elimina o segundo if
        nomeMenor = nome
        vlrMenor = preco
    if preco < vlrMenor:# pode ser eliminado com or preco < vlrMenor no if anterior
        nomeMenor = nome
        vlrMenor = preco
    if preco > 1000:
        qtdMil += 1
    resp = ''
    while resp not in 'SN':
        resp = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    if resp == 'N':break

print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temps {qtdMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeMenor} que custa R${vlrMenor:.2f}')
