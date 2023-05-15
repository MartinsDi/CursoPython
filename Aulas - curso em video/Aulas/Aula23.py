try:  # tenta
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):  # Faz quando der erro
    print(f'Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados')
else:  # Faz quando der certo, opicional
    print(f'O resultado é {r:.1f}')
finally: # Vai mostrar independente do resultado
    print('Volte sempre! Muito obrigado!')
