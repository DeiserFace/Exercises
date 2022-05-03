# Exercício 2 - Aula 15

maior = 0
menor = 1000
for c in range(1, 6):
    n = int(input('Digite o peso da {} pessoas: ' .format(c)))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print('O maior peso é {}Kg'.format(maior))
print('O menor peso é {}Kg'.format(menor))