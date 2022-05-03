# Exercício 2 - Aula 22

times = ['Grêmio', 'Bahia', 'Cruzeiro', 'Ituano', 'Chapecoense', 'Brusque', 'Náutico', 'Vasco', 'Sport', 'Londrina', 'Sampaio Corrêa', 'Criciúma', 'Operario', 'Guarani', 'Ponte Preta', 'Tombense', 'Vila Nova', 'CSA', 'Novoorizontino', 'CRB']

print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times [0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapeconse está na {times.index("Chapecoense")} posição')
