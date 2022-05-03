# Exercício 5 - Aula 12

from math import sqrt

x1=float(input('Digite a coordenada x do Ponto 1: '))
y1=float(input('Digite a coordenada y do Ponto 1: '))

x2=float(input('Digite a coordenada x do Ponto 2: '))
y2=float(input('Digite a coordenada y do Ponto 2: '))

x3=float(input('Digite a coordenada x do Ponto 3: '))
y3=float(input('Digite a coordenada y do Ponto 3: '))

sqrt(pow(x2-x1,2)+pow(y2-y1,2))
sqrt(pow(x3-x1,2)+pow(y3-y1,2))
sqrt(pow(x3-x2,2)+pow(y3-y2,2))

cond1 = True
cond2 = True
cond3 = True

if 11==0 or 12 == 0 or 13 ==0:
    cond1=False

if 11>(12+13) or 12>(11+13) or 13>(11+12):
    cond2=False

if 11<=abs(12-13) or 12<=abs(11-13) or 13<=abs(11-12) :
    cond3=False

triangulo=True

if cond1 == False or cond2==False or cond3 == False:
    triangulo = False
    print('Nenhum triângulo formado!')

if cond1 == False:
    print('Pelo menos um dos lados é igual a 0!')

if cond2 == False:
    print('Pelo menos um lado é maior que a soma dos outros dois!')

if cond3 == False:
    print('Um dos lados é menor ou igual ao módulo da diferença!')

elif 11==12==13:
    print('Triângulo equilátero.')
elif 11!=12!=13:
    print('Triangulo escaleno.')
else:    
    print('Triângulo é isóceles.')

if triangulo:
    print('Medida do lado 1 {:.2f} \nMedida do lado 2: {:.2f} \nMedida do lado 3: {:.2f}'.format(11,12,13))    