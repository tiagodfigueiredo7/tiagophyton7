


from ast import Import
import math
from multiprocessing.managers import BaseListProxy
numero = int(input('qual o numero?'))
raiz = math.sqrt (numero)
print ('a raiz do numero {} é igual a {}' .format(numero, math.ceil( raiz)))




import math
num  = int(input('Qual o Numero ?: '))
raiz = math.sqrt (num)
print ('a raiz do numero {}, é igual a {} , !!!' .format(num, math.floor(raiz)))


#math  = matematicaa
#math.ceil = arredonda pra cima 
#math.floor = arredonda pra baixo
#math.trunc = tranca o numero 
#math.pow   = potencia 
#math.sqrt  = raiz quadrada 
#math.factorial = fatoracao 


from math import sqrt, floor
num  = int(input('Qual o Numero ?: '))
raiz = sqrt (num)
print ('a raiz do numero {}, é igual a {} , !!!' .format(num, floor(raiz)))


import random
num = random.randint (one,10)
print (num)
