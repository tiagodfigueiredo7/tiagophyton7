#meu codigo é o 1

nome = input ('Qual seu nome? ')
disciplina = input ('' +nome+ ' Qual é a diciplina? ')
n1 = int ( input (''+ nome + ' qual sua nota nas atividades da diciplina ' +disciplina+ '?'))
nota = n1
print ('legal sua nota é', nota)
n2 = int (input ('' +nome+ ' qual sua nota na da prova da diciplina ' +disciplina+ '?'))
nota2 =n2
print ('A sua nota da Prova foi', nota2)
s = n1+n2
m = (n1+n2)/2
print ('Muito bom a soma da suas notas é {}, e sua media é {},' .format(s,m))

texto = input ('Aperte ENTER para descobrir se você passou')


if  m > 6.9:
     print ('Parabens {}, sua media foi {}, Vocẽ Passou !!! \n ' .format (nome, m))

else: 
    print ('Sinto muito {}, Sua media foi {},  Você não passou ! \n' .format (nome, m))
    