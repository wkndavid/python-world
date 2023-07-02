preço = float(input('Digite o preço do produto: R$ '))
novo = preço - (preço * 5 / 100)
print('O produto custa {}R$, e seu valor com 5% desconto é {}'.format(preço, novo))