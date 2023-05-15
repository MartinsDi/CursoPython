# 112 - Dentro do pacote utilidadesCev que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas
# com uma validação de dados para aceitar apenas valores que sejam monetários.
from Exercicios.Ex112.utilidadesCeV.dado import leiaDinheiro
from Exercicios.Ex112.utilidadesCeV.moeda import resumo

p = leiaDinheiro('Digite o preço: R$')
resumo(p,35,22)