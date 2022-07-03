
import random
cvz1 = str(input(' Coloque o primeiro canditado: '))
cvz2 = str(input(' Coloque o segundo: '))
cvz3 = str(input(' Coloque o terceiro: '))
cvz4 = str(input(' Coloque o quarto: '))
cvz5 = str(input(' Coloque o quinto: '))
lista = [cvz1, cvz2, cvz3, cvz4, cvz5]
escolhido = random.choice(lista)                               # choice vai ecolher entre os 5 cavaleiros
print ('o escolhido foi {}'.format(escolhido,))




