lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]
maiovalor=lista[0]
listaPares=[]
menorvalor=lista[0]
ocorrencia=0
mediaElementos=0
somaNegativo=0

for index in range(0,len(lista)):
    if maiovalor<lista[index]:
        maiovalor=lista[index]
    if menorvalor>lista[index]:

       menorvalor=lista[index]
    if lista[index]%2==0:
        listaPares.append(lista[index])   
    if lista[index]==lista[0]:
         ocorrencia+=1  
    mediaElementos+=lista[index] 
    if lista[index]<0:
     somaNegativo+=lista[index]

mediaElementos/=len(lista)


print(f'Maior valor: {maiovalor}')
print(f'Menor valor: {menorvalor}')
print(f'Lista de números pares: {listaPares}')
print(f'Números de ocorrências do primeiro elemento: {ocorrencia}')
print(f'Média elementos: {mediaElementos}')
print(f'Elementos negativos: {somaNegativo}')