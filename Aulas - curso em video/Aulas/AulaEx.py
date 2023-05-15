'''seg = int(input('Informe a lotação dos caminhões de segunda: '))
ter = int(input('Informe a lotação dos caminhões de terça: '))
qua = int(input('Informe a lotação dos caminhões de quarta: '))
qui = int(input('Informe a lotação dos caminhões de quinta: '))
sex = int(input('Informe a lotação dos caminhões de sexta: '))
media = int((seg+ter+qua+qui+sex)/5)

espaco = int((100 - media) * 2000 / 100)

print('Tinha espaço para mais {} garrafas'.format(espaco))

def recursão(num, num2):
    num *= num2
    num2-=1
    print(num,"-")
    if num2 > 0:
        recursão(num,num2)
    if num2 == 0:
        n = num2
        return n


def fatorial(numero):
    if numero == 1:
        return 1

    return numero * fatorial(numero - 1)

print(fatorial(5))'''
'''count = 0
num = 1536
msg = ''

for i in range(0 ,1537):
    msg = str(i)
    for j in msg:
        if '6' == j:
            count +=1

print(count)
import datetime

print(type(datetime.date(2012 , 1 , 1) - datetime.date(2011 , 1 , 1)))'''


def fatorial(numero):
    print(numero)
    if numero == 1:
        return 1

    return numero * fatorial(numero - 1)



print(fatorial(5))