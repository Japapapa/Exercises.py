
def jogar():
    import random

    print('****************************************')
    print('Bem-vindo ao jogo de advinhação!')
    print('****************************************')

    numerosecreto = random.randrange(1,101) 
    rodada = 1
    tentivas = 0
    pontos = 1000


    print('Qual nível de dificuldade?', numerosecreto)
    print('Nivel 1: Fácil')
    print('Nivel 2: Médio')
    print('Nivel 3: difícil')

    nivel = int(input('nivel:'))
    if (nivel == 1):
        tentivas = 20
    elif (nivel == 2):
        tentivas = 10
    else:
        tentivas = 5 

    for rodada in range(1, tentivas + 1):
        print('rodada {} de {}'.format(rodada, tentivas))

        chute = input('Digite seu numero de 1 até 100: ') 
        print('Você digitou {}'.format(chute))
        numero = int(chute)

        if(numero < 1 or numero > 100):
         print('Escolha um numero de 1 até 100!')
         continue
        

        acertou = numero == numerosecreto
        maior   = numero > numerosecreto
        menor   = numero < numerosecreto

        if (acertou):
            print(f'Você acertou! E fez {pontos}')
            break
        else:
            
            if(maior):
                print('Você errou! O seu numero foi maior que o numero secreto')  
                pontosmenos = abs(numerosecreto - numero)
                pontos = pontos - pontosmenos 
            elif(menor):
              print('Você errou! O seu numero foi menor que o numero secreto')  
            pontosmenos = abs(numerosecreto - numero)
            pontos = pontos - pontosmenos  

    rodada = rodada + 1

    print(numerosecreto)

    print('Fim de jogo')

if(__name__=='__main__'):
    jogar()