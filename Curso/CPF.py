def CPF():
    cpf = input('Digite um CPF: ')

    if any(i == '.' for i in cpf):
        cpf = cpf.replace('.', '')

    if any(i == '-' for i in cpf):
        cpf = cpf.replace('-', '')

    if len(cpf) == 11:
        if cpf.isdigit():
            return cpf
    print('CPF invalido, tente novamente!')
    CPF()


def gerar_digito(cpf, mult):
    soma = 0
    for i in cpf:
        soma += int(i) * mult
        mult -= 1
    soma = (soma * 10) % 11
    digito = 0 if soma > 9 else soma
    return str(digito)


cpf = CPF()
digito = gerar_digito(cpf[:9], 10)
digito += gerar_digito(cpf[:10], 11)

if cpf[9:] == digito:
    print('CPF valido')
else:
    print('CPF invalido')
