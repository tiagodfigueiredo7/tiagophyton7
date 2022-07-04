
import random
print ('No torneio dos Cavaleiros, Apenas um receberá a armadura de Ouro')

c1 = str(input('Quem será o primeiro Cavaleiro?: '))
c2 = str(input('Qual será o segundo cavaleiro?: '))
c3 = str(input('O terceiro cavaleiro: '))
c4 = str(input('O Ultimo cavaleiro?: '))

lista = [c1,c2,c3,c4]
print ('Os Corajosos Cavaleiros são {}, {}, {}, {} !!!'.format (c1, c2, c3, c4))

escolhido = random.choice(lista)   
print ('O primeiro Guerreiro do Zodiaco a lutar na arena é {} !'.format(escolhido))

lista.remove (escolhido)
escolhido2 = random.choice (lista)
print ('Seu adversário será {} !'.format(escolhido2))

lista2 = [escolhido, escolhido2]
w1 = random.choice (lista2)

enter1 = input ('Aperte ENTER para descobrir o primeiro vencedor!!!')

print  ('O vencedor da primeira baralha mortal é {} !!!'.format(w1))

lista.remove (escolhido2)

print ('...')

print ('Os proximos cavaleiros a lutar são: ')


print (lista[0])
print ('Contra o terrível')
print (lista[1])

w2 = random.choice(lista)

enter1 = input ('Aperte ENTER para descobrir quem irá para final com {} !!!'.format(w1))
print ('O Cavaleiro vencedor dessa luta foi {} !!!'.format(w2))

print ('Agora na grande final {} ira enfrentar {} !'.format (w1, w2))

listawinner = [w1, w2]

winner = random.choice(listawinner)

print('...')
print('...')
enter = input ('Aperte ENTER para descobrir o Vendedor!!!')

print ('O grande vencedor do torneiro que recebera a armadura de Ouro de Sagitario é {} !!!'.format(winner))

















