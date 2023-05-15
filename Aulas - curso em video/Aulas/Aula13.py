'''def calcula(num):
    for c in range(0, num):
        num = c * 4
        print('{} {}'.format(c, num))

if __name__ == "__main__":
    num = int(input('Digite um numero: '))
    calcula(num)'''
n = int(input('Digite um numero: '))
count = 0
for c in range(1, n+1,2):
    print(c)
    count += 1
print(count)
print('Fim')
#Estrutura de repetição com variavel de controle