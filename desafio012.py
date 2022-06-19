
p5 = float (input('Quanto custa um Ps5?: '))
print ('O Ps5 esta custando {}'.format(p5))
print ('Porem esta com desconto de 5%')
res = (p5*5)/100
print ('Legal você tem um desconto de R$ {:.2f}0'.format(res))
res1 = p5-res
print ('O Seu PS5 vai custar R$ {:.2f}0'.format(res1))


# Melhorando o codigo


nintendo = float(input('Quanto custa um Nintendo Switch?: R$ '))
desconto = float(input('Quanto de Desconto % ele ta? '))
result = (nintendo*desconto)/100
resultfinal = (nintendo-result)
print ('Com {}% de desconto o seu Switch vai ficar {:.2f} mais barato e vai passar de R$ {:.2f} para R$ {:.2f}'.format (desconto, result, nintendo, resultfinal ))
      
# Melhorando o codigo
 
