'''cato = float(input('Digite o cateto oposto: '))
cata = float(input('Digite o cateto adjacente: '))
a = cato ** 2
b = cata ** 2
hi = (a + b) ** (1/2)
print('O resultado da hipótenusa é: {:.2f}'.format(hi))'''
from math import hypot
cato = float(input('Digite o cateto oposto: '))
cata = float(input('Digite o cateto adjacente: '))
hi = hypot(cato, cata)
print('O resultado da hipótenusa é: {:.2f}'.format(hi))
