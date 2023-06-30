# Try, except, else e finally
a = 18
b = 'a'

try:
    c = a / b

except ZeroDivisionError as error:
    print('Divisão por zero')
    raise error

except NameError:
    print('Nome não esta definido')

except (TypeError, IndexError) as error:
    mensagem_erro = 'ERRO DESCONHECIDO'
    print('msg: ', error)
    print('Nome', error.__class__.__name__)
    raise

except Exception as error:  # trata todos os erros desconhecidos
    print('ERRO DESCONHECIDO')
    raise error


else:
    print(a / b)

finally:
    print('Finalizado')
