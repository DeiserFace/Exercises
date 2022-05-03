# Exercício 3 - Aula 16

for c in range(3,0,-1):
    senha = int(input("Senha: "))
    if senha == 123456:
        print("Olá, você. Seja bem vindo ao nosso banco!")
        break
    elif senha != 123456:
        print('Senha incorreta! Você ainda tem {} tentativa(s).'.format(c-1))
        if c ==1:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")
            break
