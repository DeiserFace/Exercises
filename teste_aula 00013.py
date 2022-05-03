# Exercício 6 - Aula 13

primeiro=int(input('Termo: '))
razao=int(input('Razão: '))

decimo=primeiro+9*razao

for c in range(primeiro, decimo+razao, razao):
    print('{}'.format(c),end='->')
print('Acabou')