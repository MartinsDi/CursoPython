# 62 - Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
print('=' * 30)
print('{:^30}'.format("GERADOR DE TERMOS DE PA"))
print('=' * 30)
primeiroTermo = int(input("Primeiro termo: "))
Razao = int(input('Razão: '))
termos = 10
count = 10
while termos > 0:
    print(primeiroTermo, end=" → ")
    primeiroTermo += Razao
    termos -= 1
    if termos == 0:
        termos = int(input('\nDeseja mostrar mais quantos termos? '))
        count += termos

print('Progressão fnalizada com {} termos mostrados.'.format(count))
print('ACABOU')

primeiro = int(input("Primeiro termo: "))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print("{} → ".format(termo),end='')
        termo+= razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
