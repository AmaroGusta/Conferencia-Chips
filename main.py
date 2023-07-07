import io


def tratar_arq(arquivo):
    with io.open(arquivo, 'r') as txt:
        texto = txt.read()
    lista = texto.split('\n')
    return lista


iniciais = tratar_arq('iniciais.txt')
vendas = tratar_arq('vendas.txt')
sobras = tratar_arq('sobraram.txt')

vendidos = 0
sobraram = 0
faltando = 0

for iccid in iniciais:
    if iccid in vendas:
        print(f'{iccid}: vendido')
        vendidos += 1
    elif iccid not in vendas:
        if iccid not in sobras:
            print(f'{iccid}: faltando')
            faltando += 1
        else:
            print(f'{iccid}: sobrou')
            sobraram += 1

for sobra in sobras:
    if sobra not in iniciais:
        print(f'{sobra}: não estava no bipe inicial')

print('------------------------------\n'
      f'Foram vendidos: {vendidos}\n'
      f'Sobraram: {sobraram}\n'
      f'Faltando: {faltando}')
