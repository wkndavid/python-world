#### Pintando parede
largura  = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura
#### A Cada 2 metros de parede se usa 1 litro de tinta
print('A dimensão da sua parede é de {}m x {}m é {}m²'.format(altura, largura, area))
print('A parede tem {}m² para pintar. A quantidade em litros de tinta é {}l'.format(area, (area/2)))