# 51 - Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão aritmetica, No final, mostre os primeiros 10 termos dessa progressão.
print('=' * 30)
print('{:^30}'.format("10 TERMOS DE UMA PA"))
print('=' * 30)
pT = int(input("Primeiro termo: "))
rz = int(input('Razão: '))
decimo = pT + (10 - 1) * rz  # pT + (10)* rz
'''for i in range(0,10):
    print(pT, end=" → ")
    pT += rz
print('ACABOU')'''

for i in range(pT, decimo + rz, rz):  # (pT, decimo, rz)
    print(i, end=" → ")
print('ACABOU')
