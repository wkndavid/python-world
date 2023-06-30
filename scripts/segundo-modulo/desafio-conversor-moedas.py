qtd = float(input('Digite um valor em real R$: '))
dolar = float(qtd / 4.82)
euro = float(qtd / 5.26)
print('A quantidade de {}R$ vale em Dolar {:2f}$ e em Euro {:2f}Є.'.format(qtd, dolar, euro))