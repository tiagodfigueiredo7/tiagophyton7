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

texto = input ('computando... computando..Aperte ENTER para descobrir se você passou')

print ('Parabens ' +nome+ ' sua media foi {},' .format(m), end='')
print (' Você Passou!!!')


# aqui eu refiz todo o processo a cima aplicando menos linhas para fazer a mesma coisa \o/
# observe na linha 28 o :.1f -  esse codigo é para ficar apenas 1 numero depois do ponto , pro resultado nao ficar gigante ex:  7.6555555

nome = input('Qual seu nome? ')
disciplina1 = input ('Legal {} qual Diciplina você esta cursando?'.format (nome))
nota8 = int(input('Qual a nota da atividade?: '))
nota9 = int(input('Qual a nota da prova?: '))
print (' Sua Nota da Atividade é {:.1f}  e sua nota da Prova é {:.1f}'.format(nota8,nota9))
media = (nota8+nota9)/2
print ('Sua media é {}'.format(media))
print ('Parabéns')