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

texto = input ('computando... computando..Aperte ENTER para descobrir se você passou')

print ('Parabens ' +nome+ ' sua media foi {},' .format(m), end='')
print (' Você Passou!!!')

