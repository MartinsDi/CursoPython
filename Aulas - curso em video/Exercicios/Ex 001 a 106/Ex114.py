# 114 - Crie um código em Python que teste se o site Pudim está acessivel pelo computador usado.
import urllib3
import urllib
import urllib.request

'''try:
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://www.orkut.com.br')
except:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')'''

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
