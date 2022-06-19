carro = input ('Qual carro você alugou? ')
print ('O carro {}, custa R$ 60.00 por dia e R$0.15 por KM rodado' .format (carro))
dia = float (input ('Quantos dias você ficou com o {}: '.format (carro)))
km = float( input ('Quantos Km o carro rodou?: '))
kmtotal = km*0.15
diatotal = dia*60
print ('Você alugou o {} e ficou com ele {:.0f} dias e rodou {} KM, o Valor a ser pago é R$ {:.2f} '.format(carro, dia, km, (kmtotal+diatotal)))



# novo codigo
carro2 = input ('Qual carro você alugou? ')
print ('O carro {}, custa R$ 60.00 por dia e R$0.15 por KM rodado!' .format(carro2))
dias = int(input ('Quantos dias o {}, rodou ?: ' .format (carro2)))
km2 = float (input ('Quantos KM o {}, rodou ?: ' .format (carro2)))
pago = (dia*60)+(km2*0.15)
print ('O carro {}, rodou {}Km em {} dias ! O Total a pagar é : R$ {:.2f}' .format(carro2, km2, dias, pago))

