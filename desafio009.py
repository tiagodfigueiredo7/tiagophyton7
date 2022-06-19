tab = int (input ('Vamos brincar de Tabuada, escolha um numero: '))
print ('Você escolheu o numero:',tab)

print ('Você quer fazer',tab , end='')
r = int (input(' X quanto?: '))
t1 = tab*r
print ('O resultado dessa multiplicação é: {}' .format(t1,))    
print ('Parabéns, porem vou mostrar a tabuada do numero escolhido completo a baixo')
m0 = tab*0
m1 = tab*1
m2 = tab*2
m3 = tab*3
m4 = tab*4
m5 = tab*5
m6 = tab*6
m7 = tab*7
m8 = tab*8
m9 = tab*9
m10 = tab*10

print ('',tab, end ='')
print (' x 0 é igual: = {}' .format(m0))  

print ('',tab, end ='')
print (' x 1 é igual: = {}' .format(m1))  

print ('',tab, end ='')
print (' x 2 é igual: = {}' .format(m2))  

print ('',tab, end ='')
print (' x 3 é igual: = {}' .format(m3)) 

print ('',tab, end ='') 
print (' x 4 é igual: = {}' .format(m4)) 

print ('',tab, end ='') 
print (' x 5 é igual: = {}' .format(m5))  

print ('',tab, end ='')
print (' x 6 é igual: = {}' .format(m6))  

print ('',tab, end ='')
print (' x 7 é igual: = {}' .format(m7))  

print ('',tab, end ='')
print (' x 8 é igual: = {}' .format(m8)) 

print ('',tab, end ='') 
print (' x 9 é igual: = {}' .format(m9))

print ('',tab, end ='')
print (' x 10 é igual: = {}' .format(m10))




# aqui outro jeito que o professor ensinou fazer o mesmo codigo
#obs usamos o :2 aqui para que a linha fique com 2 digitos para deixar mais organizado

num = int(input('Qual o numero você escolhe?: '))
print ('='*12)
print ('{} x {:2} = {}'.format(num, 1, num*1))
print ('{} x {:2} = {}'.format(num, 2, num*2))
print ('{} x {:2} = {}'.format(num, 3, num*3))
print ('{} x {:2} = {}'.format(num, 4, num*4))
print ('{} x {:2} = {}'.format(num, 5, num*5))
print ('{} x {:2} = {}'.format(num, 6, num*6))
print ('{} x {:2} = {}'.format(num, 7, num*7))
print ('{} x {:2} = {}'.format(num, 8, num*8))
print ('{} x {:2} = {}'.format(num, 9, num*9))
print ('{} x {:2} = {}'.format(num, 10, num*10))
print ('='*12)