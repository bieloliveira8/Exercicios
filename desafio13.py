salário = float(input('Qual é o salário do funcionário? R$'))
novo = salário + (salário * 15/100)
print(f'Um funcionário que ganhava R${salário:.2f}, com 15% de aumento, passa a receber R${novo:.2f}')
