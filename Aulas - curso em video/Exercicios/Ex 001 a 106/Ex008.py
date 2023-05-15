# 8 - Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

num = int(input("Digite um valor: "))
km = num/1000
hm = num/100
dam = num/10
dm = num*10
cm = num*100
mm = num*1000
print("{} metros é {} centimetros e {} milimetros".format(num, cm, mm))


