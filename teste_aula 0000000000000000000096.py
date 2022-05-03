# Exercício 5 - Aula 10

ValorCamiseta = float(input('Digite um valor: R$'))
quantidade = float(input('Quantas camisetas você irá comprar: '))

if quantidade <=5:
   desconto = ValorCamiseta - (ValorCamiseta*0.03)
   print('O valor é de R${:.2f}, e com desconto passa a ser R${:.2f}'.format(ValorCamiseta,desconto))

elif quantidade > 5 and quantidade <= 10:
    desconto = ValorCamiseta - (ValorCamiseta*0.05)
    print('O valor é de R${:.2f}, e com desconto passa a ser R${:.2f}'.format(ValorCamiseta,desconto))

elif quantidade >=10:
     desconto = ValorCamiseta (ValorCamiseta *0.07)
     print('O valor é de R${:.2f}, e com desconto passa a ser R${:.2f}'.format(ValorCamiseta,desconto))
