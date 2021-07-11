n=float(input('Digite um valor em metros: '))
km=n/1000
deca=n/100
cm=n*100
mm=n*1000
print('{} metro(s),equivale a {} centímetros e {} milímetros.'.format (n, cm, mm))
print('{} metro(s), equivale a {} kilometro e {} decametro'.format(n, km, deca))