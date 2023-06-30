def localizar(super, numero):
    for index, i in enumerate(super):
        if numero in i:
            return index
    return None


def modelar(super):
    ex = f'UPDATE USUARIO SET cod_usuario_superior = {super[0]} WHERE COD_USUARIO in ({super[1]}'
    cod = ''
    for op in super:
        if op == super[0] or op == super[1]:
            continue
        cod += ', '+str(op)
    ex += cod + ')'
    return ex

def super(listas):
    super = []

    for lista in listas:
        if len(super) == 0:

            ope = [lista[1], lista[0]]
            super.append(ope.copy())
            ope.clear()

        else:
            pos = localizar(super, lista[1])
            if pos is not None:
                super[pos].append(lista[0])

            else:
                ope = [lista[1], lista[0]]
                super.append(ope)
    return super



