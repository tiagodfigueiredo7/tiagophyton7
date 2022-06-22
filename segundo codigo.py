nome = input ('Qual o nome do Aluno ?: ' )
ano_escolar = int (input ('Qual o ano do {} ? 6 a 9 serie ?: ' .format (nome)))

if (ano_escolar < 5 or ano_escolar > 9):
    print ('Esse ano escolar não existe!')

else:  
    
    nota1 = float(input ('Qual a Nota do Aluno {}: ' .format (nome)))
    nota2 = float (input ('Qual a Segunda nota do Aluno {}: ' .format (nome)))
    media = (nota1+nota2)/2
    media_final = float (media)
    

    if (( ano_escolar > 4 )) and ((ano_escolar < 9)):
        if media_final > 6.9:
            print ('Parabéns {}, Sua Nota foi boa {} e Você passou!'.format (nome, media))
        elif media_final == 6:
            print ('O Aluno {}, ficou de recuperação : {}'.format (nome, media))
        elif media_final < 6:
            print ('Você repetiu com a media de : {} !!! '.format (media))

    elif  ano_escolar == 9:
        if media_final > 6.9: 
            print ('Parabéns {}, sua nota foi {:.1f} ! Vocẽ passou !! ' .format(nome, media))
        if media_final < 7:
            print ('{}, sua nota foi {:.1f} você repetiu !' .format(nome, media))