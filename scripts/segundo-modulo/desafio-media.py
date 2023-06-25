##########################################################################
#  Exercício de média aritimética, média escolar de notas de 4 semestre  #
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
n4 = float(input('Digite sua quarta nota: '))

med = (n1 + n2 + n3 + n4) / 2

print('A média entre as notas é : {}'.format(med))

if med >= 10:
    print('Aprovado')
else:
    print('Reprovado. A média mínima é de 20 pontos para aprovação :(, estude mais!')