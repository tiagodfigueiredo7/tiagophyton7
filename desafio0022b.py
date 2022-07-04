
# melhorando mais ainda o codigo


nome = input ('Qual seu nome? : ').strip()  # usamos o strip aqui em cima para que corte os espaços na conta do len
print ('Ola {} '.format(nome))
print ('seu nome em letras maiucuslas é {}'.format(nome.upper()))
print ('seu nome em letras minusculas é {}'.format(nome.lower()))
print ('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print ('Seu primeiro nome tem {} letras '.format(nome.find(' ')))         #aqui usando o findo para encontrar e trazer informações
div = nome.split()                                                    # aqui usamos o div=nome.slip para separar os nomes em tableas
print ('Seu nome do meio é {}' .format(div[1]))                            # aqui usamos o print completo fazendo o nome do meio
print ('seu nome do meio é {} e tem {} letas'.format(div[1], len(div[1])))



               