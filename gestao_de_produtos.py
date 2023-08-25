valor_unit = float(input('Entre com o valor do produto:')) # valor_unit recebe numeros com casas decimais (float)
quantidade = int(input('Entre com a quantidade do produto:')) # quantidade recebe numeros inteiros (int)

# Aqui é definido o valor do desconto em relaçao a quantidade de produtos
if quantidade < 200: 
    desconto = 0
elif quantidade >= 200 and quantidade < 1000: 
    desconto = 0.05
elif quantidade >= 1000 and quantidade < 2000: 
    desconto = 0.10
else:
    desconto = 0.15 

# Calculos para exibiçao sem e com desconto.
valor_sem_desconto = valor_unit * quantidade 
valor_com_desconto = valor_sem_desconto - (valor_sem_desconto * desconto)


print ('O valor SEM desconto: R$ {}'.format(valor_sem_desconto))
print ('O valor COM desconto: R$ {}'.format(valor_com_desconto))
