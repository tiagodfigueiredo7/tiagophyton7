

nome = input ('Qual o nome do Aluno ?: ' )
ano_escolar = int (input ('Qual o ano do {} ? 6 a 9 serie ?: ' .format (nome)))

if (ano_escolar < 5 or ano_escolar > 9):
    print ('Esse ano escolar não existe!')

else:
     
    nota1 = float(input ('Qual a Nota do Aluno {}: ' .format (nome)))
    
    if nota1 >= 7: 
        print ('Muito bom {} continue assim !!! '.format (nome))
        
    else:
        print ('Que porcaria de nota é essa {} ? Melhore isso !!!' .format(nome))    
    
    
    nota2 = float (input ('Qual a Segunda nota do Aluno {}: ' .format (nome)))
    media = (nota1+nota2)/2
    media_final = float (media)
    

    if (( ano_escolar > 4 )) and ((ano_escolar < 9)):
        if media_final > 6.9:
            print ('Parabéns {}, Sua Nota foi boa {} e Você passou!'.format (nome, media))
        elif media_final == 6:
            print ('Sinto muito {} , você é mto Burro e ficou de recuperação com a media de : {:1.f}'.format (nome, media_final))
        elif media_final < 6:
            print ('Vai troxa, não estudou né? Quem mandou....Você repetiu com a media de : {:1.f} !!! '.format (media))

    elif  ano_escolar == 9:
        if media_final > 6.9: 
            print ('Parabéns {}, sua nota foi {:.1f} ! Vocẽ passou !! ' .format(nome, media))
        if media_final < 7:
            print ('Sinto Muito {}, sua nota foi {:.1f} e não aceitamos pessoas burras aqui !' .format(nome, media))
                   