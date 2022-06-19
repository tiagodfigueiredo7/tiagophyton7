# aqui tivemos que usar o float em vez de int, porque vamos usar numeros  ex:  2.5 2.7 2.8 


tinta = float(input('Qual a largura da parede: '))
print ('a largura da parede é {}'.format(tinta))
tinta2 = float(input('Qual a altura da parede: '))
print ('a altura da parede é {}'.format (tinta2))
m2 = tinta*tinta2
print ('A parede que vamos pintar tem {} metros²'.format(m2))
print ('1 litro de tinta pinta uma área de 2m²')
resultado = m2/2
print ('Vamos precisar de {} litros de tinta para pintar toda parede'.format(resultado))
                                                                             




2