# 97 - faça um programa que tenha um afuncção chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#ex: escreva ('Olá, mundo!')
# saida ~~~~~~~~~~~~~~
        #Olá, mundo!
    #~~~~~~~~~~~~~~~~

def escreva(txt):
    cont = len(txt)+4
    print('~'*cont)
    print(f"  {txt}")
    print('~'*cont)


escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva("CeV")
