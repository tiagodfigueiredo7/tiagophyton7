nome = input('Qual seu nome? : ')
print ('Ola {}'.format(nome))
nome2 = nome.upper()
print ('Seu nome em letras Maiusculas é {}' .format(nome2))
nome3 = nome.lower()
print ('seu nome em letras minusculas é {}'.format(nome3))
letras =  (len(nome.strip()))
print ('Seu nome tem {} letras'.format(letras))
div = nome.split()
print (div[0])


#novo codigo 

nome = input ('Qual seu nome? :')
print ('Ola {} '.format(nome))
print ('seu nome em letras maiucuslas é {}'.format(nome.upper()))
print ('seu nome em letras minusculas é {}'.format(nome.lower()))
print ('seu nome tem ao todo {}'.format(len(nome.strip())))                  # strip faz nao contar os espaços 


# Melhorando o codigo 

nome = input ('Qual seu nome? :').strip()  # usamos o strip aqui em cima para que corte os espaços na conta do len
print ('Ola {} '.format(nome))
print ('seu nome em letras maiucuslas é {}'.format(nome.upper()))
print ('seu nome em letras minusculas é {}'.format(nome.lower()))
print ('seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')))
print ('Seu primeiro nome tem {}  letras '.format(nome.find(' ')))         #aqui usando o findo para encontrar e trazer informações
div = nome.split()                                                    # aqui usamos o div=nome.slip para separar os nomes em tableas
print ('Seu nome do meio é {}' .format(div[1]))                            # aqui usamos o print completo fazendo o nome do meio


