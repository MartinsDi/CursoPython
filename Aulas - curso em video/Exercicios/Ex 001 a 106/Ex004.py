
var = input('Digite algo: ')

print('O tipo primitivo desse valor é {}'.format(type(var)))
print('Só tem espaço? {}'.format(var.isspace()))
print('É um numerico? {}'.format(var.isnumeric()))
print('É alfabético? {}'.format(var.isalpha()))
print('É alfanumerico? {}'.format(var.isalnum()))
print('Está em maiúsculas? {}'.format(var.isupper()))
print('Está em minúsculas? {}'.format(var.islower()))
print('Está capitalizada? {}'.format(var.istitle()))

