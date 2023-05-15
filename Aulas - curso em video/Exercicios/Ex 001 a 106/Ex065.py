# 65 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = 0
count = 0
per = 'S'
while per == 'S':
    num = int(input('Digite um numero: '))
    count += 1
    soma += num
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    per = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
media = soma / count
#print('A media dos numeros é {:.2f}\nO maior numero é {}\nO menor numero é {}'.format(media,maior,menor))
print('Você digitou {} números e a média foi {}'.format(count,media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
