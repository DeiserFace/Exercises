# Exercício 4 - Aula 13

tabuada=int(input("Tabuada do numero determinado: "))
for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )
