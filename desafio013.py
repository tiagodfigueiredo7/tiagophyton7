salario = int(input('Qual o seu salario?: '))
print ('Seu salario é {} e você teve um aumento de 15%'.format(salario))
resultado = (salario*15)/100
print ('Você teve um aumento de {}0'.format(resultado))
resultado2 = resultado+salario
print ('Agora você recebe R$ {}0'.format(resultado2))
print ('...')
print ('...')
novosalario =int(input('Se você tiver outra % de aumento baseado no novo salario, como seriam os valores atualizados?  coloque a nova %: '))
resultado3 = (resultado2*novosalario)/100
resultadofinal = resultado2+resultado3
print ( 'Com esses aumentos você teria um ganho de R$ {}0 e um salario de {}0'.format(resultado3, resultadofinal))

      