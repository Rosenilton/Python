d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos KM este carro foi rodado? '))
total = (d * 60) + (km * 0.15)
print('O valor total do aluguel deste veiculo foi de R$ {:.2f}.'.format(total))