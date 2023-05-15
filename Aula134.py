pessoa = {'nome': 'Aline', 'sobrenome': 'Souza'}

dados_pessoa = {'idade' : 16, 'altura': 1.6}

pessoa_completa = {**pessoa, **dados_pessoa, 'sexo': 'f'}
#print(pessoa_completa)

def mostra_argumento_nomeado(*args, **kwargs):
    print('Não nomeado', args)
    for chave, valor in kwargs.items():
        print(chave, valor)


mostra_argumento_nomeado(**pessoa_completa)
mostra_argumento_nomeado(nome= 'Joana', qLq=123)