# \033[ STYLE ; TEXT ; BACK m (ordem não importa
# STYLO = 0 (NONE), 1(Bold), 4 (underline), 7 (negativo)
# TEXT = 30 branco, 31 vermelho, 32 verde, 33 amarelo, 34 azul , 35 magenta, 36 ciano, 37 cinza
# BACK = 40 branco, 41 vermelho, 42 verde, 43 amarelo, 44 azul , 45 magenta, 46 ciano, 47 cinza
# modulo colorize
'''print('\033[0;30;41mTeste')
print('\033[4;33;44mTeste')
print('\033[1;35;43mTeste')
print('\033[30;42mTeste')
print('\033[mTeste')
print('\033[7;30mTeste')'''

# print('\033[7;33;44mOlá mundo!\033[m')
nome = 'Diego'
cores = {'Limpa': '\033[m', 'azul': '\033[34m', 'amarelo': '\033[33m', 'pretoebranco': '\033[7;30m'}
#print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['Limpa']))
