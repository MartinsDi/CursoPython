# 77 - Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.
lista = ('aprender', "programar",'linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')

for i in lista:
    print(f'\nNa palavra {i.upper():15} temos', end='')
    for c in i:
        if c.lower() in 'aeiou':
            print(f' {c}',end='')