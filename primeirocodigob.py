
dinheiro = float(input( 'Quanto você tem para gastar:? R$ '))
item = (input('O que você quer comprar?: '))
valor = float (input('Qual o valor do ' +item+ '? : R$ '))

s = valor - dinheiro

if dinheiro < valor:
    print ('Desculpe, Você nao consegue comprar o {} com {:.2f}, vai faltar {:.2f}, junte mais dinheiro !' .format(item, dinheiro, s)) 
    
else:  
    print ('Com {:.2f} você consegue comprar o {} '. format(dinheiro, item))

