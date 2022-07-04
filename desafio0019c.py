
import random
cvz1 = str(input(' Coloquei o primeiro lutador: '))
cvz2 = str(input(' Coloque o segundo: '))
cvz3 = str(input(' Coloque o terceiro: '))
cvz4 = str(input(' Coloque o quarto: '))
cvz5 = str(input(' Coloque o quinto: '))
lista = [cvz1, cvz2, cvz3, cvz4, cvz5]
escolhido = random.choice(lista)   
escolhido2 = random.choice(lista)   # choice vai ecolher entre os 5 cavaleiros
print ('O cavaleiro escolhido para primeira luta foi  {}'.format(escolhido,))
print ('..')
print ('O Outro cavaleiro  escolhido foi  {}'.format(escolhido2,))
lista2 = [escolhido,escolhido2]
print ('O vencedor da primeira luta foi {} !!!' .format(lista2))





