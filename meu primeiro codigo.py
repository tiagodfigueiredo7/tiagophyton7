dinheiro = float(input( 'Quanto você tem para gastar:? R$ '))
item = (input('O que você quer comprar?: '))
valor = float (input('Qual o valor do ' +item+ '? : R$ '))
print ('Pagando a vista o {} tem 8.5% de desconto e pagando em 12x no Cartão um acrecimo de 3.85% ao mês'. format(item,))
desconto = (valor*8.5)/100
jurosmes = (valor*3.85)/100
jurosano = ( jurosmes*12)
print ('Se você comprar o {} a vista ira economizar R$ {:.2f} e irá pagar R$ {:.2f} no total'.format(item, desconto, (valor-desconto)))
print ('Porém se resolver pagar em 12x, pagara R$ {:.2f} a mais por mês, R$ {:.2f} a mais no final e irá pagar R$ {:.2f} no total'.format(jurosmes, jurosano, (jurosano+valor)))
print ('')
total1 = (valor-desconto)
total2 = (valor + jurosano)
print ('Você tinha um saldo de R$ {:.2f} e comprando {} ficou com R$ {:.2f} no final se comprou a vista' .format (dinheiro, item, (dinheiro-total1)))
print ('mas...')
print ('Você tinha um saldo de R$ {:.2f} e comprando {} ficou com R$ {:.2f} no final se comprou a em 12x ' .format (dinheiro, item, (dinheiro-total2)))