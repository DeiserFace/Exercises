# Exercício 1 - Aula 19

n = int(input('Digite um número inteiro: '))
n1 = 0
n2 = 1
print(f'{n1,n2}',end = '-')

for c in range(n):
    n3 = n1 + n2
    print(f'{n3}', end='-')
    n1 = n2
    n2 = n3