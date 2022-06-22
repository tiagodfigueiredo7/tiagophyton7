dinheiro = float(input( 'Quanto você tem para gastar:? R$ '))
item = (input('O que você quer comprar?: '))
valor = float (input('Qual o valor do ' +item+ '? : R$ '))

s = valor - dinheiro



if  dinheiro > valor:
    print ('Com R$ {:.2f} vocẽ consegue comprar {} !' .format( dinheiro, item))
           
else: 
    print  ('Infelizmente os R$ {:.2f} não serão suficientes , vai faltar R$ {:.2f}! Junte mais dinheiro !'.format (dinheiro, s))
    
    