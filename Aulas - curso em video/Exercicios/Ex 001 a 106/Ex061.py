# 61 = Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('=' * 30)
print('{:^30}'.format("GERADOR TERMOS DE PA"))
print('=' * 30)
pT = int(input("Primeiro termo: "))
rz = int(input('Razão: '))
decimo = 10

while decimo > 0:
    print(pT, end=" → ")
    pT += rz
    decimo -= 1

print('ACABOU')
