# ctrl + D duplica a linha
#print('824','176','070', sep='.', end='-')
#print('18')

#num1 = int(input())
#num2 = int(input())
#num3 = num1 + num2
#print(num3)

#num1 = 125522

#print(f'{num1:.1d}')

num = int(input('Digite um numero: '))

while num > 0:
    if num % 2 == 0:
        num -= 1
    else:
        num -= 2
    print(num)

