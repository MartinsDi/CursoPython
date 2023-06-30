from Leitura import Listas, permissao
import Metodos as m


listas = Listas()



with open('celula.txt', 'a') as celula:
    for linha in listas:
        celula.write(f'({linha[2]},{linha[0]},1,getdate(),null),')


with open('permissao.txt', 'a') as pms:
    for linha in listas:
        pms.write(f'({linha[0]}, {permissao}),')


with open('update.txt', 'a') as sup:
        super = m.super(listas)
        for ope in super:
            update = m.modelar(ope)
            sup.write(update+"\n")