n1= input('Digite algo: ')
print('O tipo primitivo de {} é'.format(n1), type(n1))
print('É um valor alphanúmerico? ',n1.isalnum())
print('É um valor alfabétipo? ',n1.isalpha())
print('É um valor que pode ser impresso? ',n1.isascii())
print('É um numero? ', n1.isnumeric())
print('Este valor tem somente espaços? ', n1.isspace())
print('Está em maiúsculas? ', n1.isupper())
print('Está em minúscula? ', n1.islower())
print('Está capitalizado? ', n1.istitle())