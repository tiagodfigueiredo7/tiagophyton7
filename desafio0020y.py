
import random
cvz1 = str(input(' Coloque o primeiro lutador?: '))
cvz2 = str(input(' Coloque o segundo: '))
cvz3 = str(input(' Coloque o terceiro: '))
cvz4 = str(input(' Coloque o quarto: '))
cvz5 = str(input(' Coloque o quinto: '))
lista = [cvz1, cvz2, cvz3, cvz4, cvz5]
random.shuffle(lista)                                        # aqui é usado o suffle para enbaralhar  as opções e trazer na ordem
print ('o escolhido foi {}'.format(lista))



from random import shuffle
cvz1 = str(input(' Coloque o primeiro lutador?: '))
cvz2 = str(input(' Coloque o segundo: '))
cvz3 = str(input(' Coloque o terceiro: '))
cvz4 = str(input(' Coloque o quarto: '))
cvz5 = str(input(' Coloque o quinto: '))
lista = [cvz1, cvz2, cvz3, cvz4, cvz5]
shuffle(lista)                                         # aqui é usado o suffle para enbaralhar  as opções e trazer na ordem
print ('o escolhido foi {}'.format(lista))

