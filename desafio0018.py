import math
angulo = float(input('Digite o angulo que vc deseja '))
seno   = math.sin(math.radians(angulo))
print  ('O Angulo de {} tem o SENO de {}'.format (angulo, seno))
cosseno = math.cos(math.radians(angulo))
print ('o Angulo de {} tem o cosseno de {}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print ('O angulo de {} tem a tangente de {}'.format(angulo, tangente))




# aqui usei o from math e o import para radians, sin , cos e tan, pra ser outra maneira de executar

from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que vc deseja '))
seno   = sin(math.radians(angulo))
print  ('O Angulo de {} tem o SENO de {}'.format (angulo, seno))
cosseno = cos(math.radians(angulo))
print ('o Angulo de {} tem o cosseno de {}'.format(angulo, cosseno))
tangente = tan(math.radians(angulo))
print ('O angulo de {} tem a tangente de {}'.format(angulo, tangente))

