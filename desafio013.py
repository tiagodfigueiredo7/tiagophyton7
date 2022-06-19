salario = float(input('Qual o seu salario? R$: '))
print ('Seu salario é {} e você teve um aumento de 15%'.format(salario))
resultado = (salario*15)/100
print ('Você teve um aumento de {}0'.format(resultado))
resultado2 = resultado+salario
print ('Agora você recebe R$ {}0'.format(resultado2))
print ('...')
print ('...')
novosalario = float(input('Se você tiver outra % de aumento baseado no novo salario, como seriam os valores atualizados?  coloque a nova %: '))
resultado3 = (resultado2*novosalario)/100
resultadofinal = resultado2+resultado3
print ( 'Com esses aumentos você teria um ganho de R$ {}0 e um salario de {}0'.format(resultado3, resultadofinal))

      
      
# melhorando o codigo

salario2 = float (input('Qual o seu Salario ?R$: '))
novo = salario2 + (salario*15)/100
print ('...')
print ('Seu Salario atual é R$ {:.2f}, você teve um aumento de {:.2f}%, com isso você irá receber R$ {:.2f}'.format(salario2, 15, novo,))
3