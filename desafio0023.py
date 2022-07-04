
numero = int(input('Digite um numero de 1 a 9999:' ))
n = str(numero)
print ('Analisando o numero {}'.format(numero))

if (numero > 9999 or numero < 1):
   print ('Esse numero nao pode !!!')
    
else:
   print('A unidade é {}'.format(n[3]))
   print('A dezena  é {}'.format(n[2])) 
   print('A centena é {}'.format(n[1]))
   print('O Milhar é {}'.format(n[0]))
