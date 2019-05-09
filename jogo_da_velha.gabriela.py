def print_tab(c1, c2, c3, c4, c5, c6, c7, c8, c9):
    print ((' %s | %s | %s \n' +\
            '----+----+----\n' +\
            ' %s | %s | %s \n' +\
            '----+----+----\n' +\
            ' %s | %s | %s \n') % (c1, c2, c3, c4, c5, c6, c7, c8, c9))

def tem_ganhador (vez, c1, c2, c3, c4, c5, c6, c7, c8, c9):
    if c1 == c2 == c3 or c4 == c5 == c6 or c7 == c8 == c9 or \
    c1 == c4 == c7 or c2 == c5 == c8 or c3 == c6 == c9 or \
    c1 == c5 == c9 or c3 == c5 == c7:
        print ("o Jogador %s ganhou " % ('O' if vez == 'X' else 'X'))
        return True
    else:
        return False

def deu_velha(c1, c2, c3, c4, c5, c6, c7, c8, c9):
    if c1 != '1' and c2 != '2' and c3 != '3'and\
       c4 != '4' and c5 != '5' and c6 != '6'and\
       c7 != '7' and c8 != '8' and c9 != '9':
       print (" deu velha")
       return True
    else:
        return False

def valida_jogada(c, c1, c2, c3, c4, c5, c6, c7, c8, c9):

    if (c == '1' and c1 != '1') or \
       (c == '2' and c2 != '2') or \
       (c == '3' and c3 != '3') or \
       (c == '4' and c4 != '4') or \
       (c == '5' and c5 != '5') or \
       (c == '6' and c6 != '6') or \
       (c == '7' and c7 != '7') or \
       (c == '8' and c8 != '8') or \
       (c == '9' and c9 != '9'):
        print("casa ocupada")
        return False
    else:
        return True

def jog(c1, c2, c3, c4, c5, c6, c7, c8, c9):
    jogador = input("Qual jogador você quer ser? ")

    while  not (jogador.lower() == 'x' or  jogador.lower() == 'o'):
        print("Jogador inválido.....")
        jogador = input("Qual jogador você quer ser? ")
    vez = jogador.upper()

    print_tab(c1, c2, c3, c4, c5, c6, c7, c8, c9)
    while not tem_ganhador(vez, c1, c2, c3, c4, c5, c6, c7, c8, c9) and\
            not deu_velha(c1, c2, c3, c4, c5, c6, c7, c8, c9):

        c = str(input("jogador %s escolhe sua jogada: " % vez))
        while not valida_jogada(c, c1, c2, c3, c4, c5, c6, c7, c8, c9):
            c = int(input("jogador %s escolhe sua jogada: " % vez))
        if c == '1': c1 = vez    
        elif (c == '2'): c2 = vez
        elif (c == '3'): c3 = vez
        elif (c == '4'): c4 = vez
        elif (c == '5'): c5 = vez
        elif (c == '6'): c6 = vez
        elif (c == '7'): c7 = vez
        elif (c == '8'): c8 = vez
        elif (c == '9'): c9 = vez

        print_tab(c1, c2, c3, c4, c5, c6, c7, c8, c9)
        
        vez = 'X' if vez == 'O' else 'O'

jogo = True                    
while jogo:
    jog(*(str(i) for i in range(1, 10)))
    jogo = input("Quer jogar de novo? (s/n) ") in 'sS'
    
