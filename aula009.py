frase = "curso em video  Python"
print (frase[2:15])       


frase = "curso em video  Python"
print (frase[4:15:2])                  # o 4 é onde começa , o 15 é onde termina, e o 2 é pulando de 2 em 2 a partir do 4:

print ("oi")



# aqui em vez de usar print em cada linha, podemos colocar """ e """ para ele imprimir o texto inteiro 
print ("""Profissional com mais de 15 anos de experiência na área de Tecnologia da Informação em grandes empresas do
mercado. Sólidos conhecimentos em desenvolvimento de soluções tecnológicas interligadas as necessidades
estratégicas da empresa com foco na garantia de ambiente de alta disponibilidade. Responsável por infraestrutura
AWS. Me especializando na área de DevOps, Cloud, Docker e Terraform""")


frase = "curso em video  Python"
print (frase.count('o'))                   # aqui ele vai usar o frase.count'o' para contar quantas vezes a letra o aparece na frase



frase = "curso em video  Python"
print (frase.upper().count('P'))                # aqui usamos o upper para contar letras maiusculas



frase = "curso em video Python"
print (frase.replace('Pyhton','android'))       # aqui usamos o comando replace para trocar palavras 

frase = "curso em video Python"
print (frase.find('video'))


frase = "curso em video Python"
print (frase.split())                      # aqui ele vai separar cada palavra da frase



frase = "curso em video Python"
div   = frase.split()                  # aqui estamos criando uma variable para que dentro da frase, ele escolha qual palavra
print (div[3][4])

