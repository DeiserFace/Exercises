# Exercício 3 - Aula 19

p = 'S'
s = c = 0
maior = 0
while p == 'S' :
    n = int(input('Digite um número: '))
    p = str(input('Quer continuar? [S/N] ')).strip().upper()
    while p != 'S' and p != 'N' :
        p = str(input('Digite S ou N. Quer continuar? [S/N] ')).strip().upper()
    s += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Média: ', s/c)
print('Maior: ', maior)
print('Menor: ', menor)            
    

