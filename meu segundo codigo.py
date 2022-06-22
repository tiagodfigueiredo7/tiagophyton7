

nome = input ('Qual o nome do Aluno ?: ' )
ano_escolar = int (input ('Qual o ano do Aluno  6 serie a 9 serie ? '))

if (ano_escolar < 5 or ano_escolar > 9):
    print ('Esse ano escolar não existe!')

else:
     
    nota1 = float (input ('Qual a Nota do Aluno {}: ' .format (nome)))
    nota2 = float (input ('Qual a Segunda nota do Aluno {}: ' .format (nome)))
    media = (nota1+nota2)/2
    media_final = float (media)
    

    if (( ano_escolar > 4 )) and ((ano_escolar < 9)):
        if media_final >= 7:
            print ('Parabens {}, Sua Nota foi boa {} e Você passou!'.format (nome, media))
        elif media_final == 6:
            print ('Sinto muito {} , você é mto Burro e ficou de recuperação'.format (nome))
        elif media_final < 6:
            print ('Vai troxa, não estudou né?  quem mandou....')

    elif  ano_escolar == 9:
        if media_final >= 7: 
            print ('Parabens {}, sua nota foi {} ! Vocẽ passou !! ' .format(nome, media))
        if media_final <= 6:
            print ('Sinto Muito {}, sua nota foi {} e não aceitamos pessoas burras aqui' .format(nome, media))
                   