
# fazendo do jeito dificil

num   = float (input('Qual o cateto oposto?: '))
num2  = float (input('Qual a adjacente?: '))
num3  =  (num **2 + num2** 2) **(1/2)

print ('O resultado é {}'.format(num3))
           


# fazendo do jeito facil , usando o import math, e usando o math.hypot par ele ja fazer a conta 
#Faça um programa que colete o cateto oposto e o adjacente e cacule a hipotenusa --> math.hypot

import math
num   = float (input('Qual o cateto oposto?: '))
num2  = float (input('Qual a adjacente?: '))
num3  = math.hypot (num, num2)
print ('o resultado sera {}'.format (num3))

