def jogarMortalQueen():

    print("\r\n" '''                .,aadd"'    `"bbaa,.
            ,ad8888P'          `Y8888ba,
         ,a88888888              88888888a,
       a88888888888              88888888888a
     a8888888888888b,          ,d8888888888888a
    d8888888888888888b,_    _,d8888888888888888b
   d88888888888888888888888888888888888888888888b
  d8888888888888888888888888888888888888888888888b
 I888888888888888888888888888888888888888888888888I
,88888888888888888888888888888888888888888888888888,
I8888888888888888PY8888888PY88888888888888888888888I
8888888888888888"  "88888"  "88888888888888888888888
8::::::::::::::'    `:::'    `:::::::::::::::::::::8
Ib:::::::::::"        "        `::::::' `:::::::::dI
`8888888888P            Y88888888888P     Y88888888'
 Ib:::::::'              `:::::::::'       `:::::dI
  Yb::::"                  ":::::"           "::dP
   Y88P                      Y8P               `P
    Y'                        "
                                `:::::::::::;8"
       "888888888888888888888888888888888888"
         `"8;::::::::::::::::::::::::::;8"'
            `"Ya;::::::::::::::::::;aP"'
                ``""YYbbaaaaddPP""''   ''' "\r\n")



    print("-="*27)
    print("=-"*6, "BEM-VINDO AO MORTAL QUEEN ", "=-"*7)
    print("-="*27, "\n")

    print('''
    Em uma viagem ao Egito, o seu melhor amigo, o Kaleo, desapareceu. 
    Após procurar pistas do seu paradeiro por vários lugares na cidade, um Guia Turístico local
    disse ter visto alguém parecido com Kaleo, perto da pirâmide Quéops.
    ''')

    print('''
    Uma senhora misteriosa passou ao seu lado na rua e disse que para encontrar o que procura é preciso
    primeiro deixar-se encontrar.
    Sem entender, você tenta pedir detalhes. A mulher desaparece diante dos seus olhos como num passe de mágica.
    Mas deixa cair uma moeda com a face de Cleópatra.
    Você guarda a moeda.
    ''')

    print('''
    O delegado da cidade disse que as buscas nos locais sagrados estão proibidas porque a maldição de
    Hatshepsut é forte demais e as armas humanas não conseguem superar.
    Você não pensa duas vezes e decide desvendar o mistério com ou sem ajuda.
    Que maldição seria esta?

    Qual das mais poderosas Rainhas do Egito está por trás disso?
    Os Deuses aconselham que se apresse pra descobrir!
    Não há tempo a perder!
    ''')

    print('''
    Só estas 3 pessoas no Cairo são capazes de conseguir salvar Kaleo, mas você deve escolher apenas uma.:

    Joanna é curiosa, pratica escalada e não perde a oportunidade de desvendar um mistério.

    Luan é bom em raciocinar rápido, nada bem e corre como um guepardo.

    Hannah é observadora, muito corajosa e contorcionista em um circo famoso.
    ''')


    jogador1 = "Joanna"
    print("1.", jogador1, "\n")
    jogador2 = "Luan"
    print("2.", jogador2, "\n")
    jogador3 = "Hannah"
    print("3.", jogador3, "\n")

    jogadorEscolhido = input("Digite o nome do seu jogador: \n".lower().capitalize())


    while jogadorEscolhido.lower().capitalize() != jogador1 and jogadorEscolhido.lower().capitalize() != jogador2 and jogadorEscolhido.lower().capitalize() != jogador3:
        print("O nome digitado não corresponde a um jogador. Tente novamente.\n")
        jogadorEscolhido = input("Digite o nome do seu jogador: \n".lower().capitalize())
        if jogadorEscolhido.lower().capitalize() == jogador1:
            print("Olá, Joanna! Prepare-se para começar a aventura!\n")
            break
        elif jogadorEscolhido.lower().capitalize() == jogador2:
            print("Olá, Luan! Prepare-se para começar a aventura!\n")
            break
        elif jogadorEscolhido.lower().capitalize() == jogador3:
            print("Olá Hannah! Prepare-se para começar a aventura!\n")
            break


    print(''' 
                              A
                             /_\ 
                     :      /_|_\ 
                    :::    /|__|_\ 
                   ::.::  /|_|__|_\      :
                  ::.:.::/__|_|__|_\    :.:
                 :..:.:./_|__|__|__|\  :.:.:
                :.:..:./|__|___|__|__\:.:..::
 ..............::..:../__|___|__|___|_\..:..::................
    ..........:..:..:/_|__|___|___|___|\:..:..::::::::::::::::::::
::::::::::::::.:..:./___|___|___|___|___\....................
        .........../..!...!...!...!...!..\...............
                                          -varian-
    ''')


    print('''
    Você chega às Pirâmides de Gizé. E entra na maior delas: Quéops.
    ''')

    escada = 1
    porta = 2
    charada1 = "Charada:\n Uns tem 4 fases.\n Outros tem 2 lados.\n Por que 2 se posso ter 18?\nResponda o que eu sou.\n"


    print(f'''{jogadorEscolhido.lower().capitalize()}, ao seu lado esquerdo há uma escada para o subsolo e
    ao seu lado direito uma grande porta.\r\n''')

    cena1 = int(input("Qual caminho você escolhe? Digite 1 / 2: \r\n"))

    if cena1 == escada:
        print("A escada tem apenas 7 degraus e você caiu no calabouço cheio de jacarés. FIM DE JOGO.")
        # repetirJogo1 = input("Deseja jogar novamente? [S / N]")
        # if repetirJogo1.upper() == "S":
        #     jogar()
        # else:
        #     print("Até a próxima!")
    elif cena1 == porta:
        print("Você entrou no Salão das Pinturas. Aqui elas tem vida e decidem o seu futuro!")
        print("A pintura de Nefertiti tem uma charada para você!")
        print("A terra sob seus pés também está viva e se você não acertar a charada,\na Deusa ordenará que seja engolido pela areia movediça.\r\n")
        print(charada1)
        respostaCharada1 = input("Digite sua resposta: ")
    else:
        print("O número digitado não corresponde a uma ação no jogo. Digite 1 ou 2.")
        cena1 = int(input("Qual caminho você escolhe? Digite 1 / 2: "))               


    if respostaCharada1.lower() == "octodecágono":
        print("Você acertou! Ganhou uma pista. Siga para o Sarcófago.")
    else:
        print("Você errou. Está afundando na Sala das Pinturas. FIM DE JOGO.")
        # repetirJogo2 = input("Deseja jogar novamente? [S / N]")
        # if repetirJogo2.upper() == "S":
        #     jogar()
        # elif repetirJogo2.upper() == "N":
        #     print("Até a próxima!")
        # else:
        #     print("Opção não disponível. Tente novamente.")
        #     repetirJogo2 = input("Deseja jogar novamente? [S / N]")
        #     if repetirJogo2.upper() == "S":
        #         jogar()
        #     if repetirJogo2.upper() == "N":
        #         print("Até a próxima!")


    print('''
    Pista:
    "sob o pé direito de Rainha ele está.
    Ninguém poderia, aos seus encantos, relutar?"
    Quem quanto mais distante ficar,
    mais perto dela estará?"
    ''')


    print('''
    .______________________________________________________________________________.
    |       _    _         _    _        _    _         _    _        _    _       |
    |  /}    \/}/     /}    \/}/     /}   \/}/     /}    \/}/     /}   \/}/     /} |
    |_/|\_    |_    _/|\_    |_    _/|\_   |_    _/|\_    |_    _/|\_   |_    _/|\_|
    | / \     | \    / \     | \    / \    | \    / \     | \    / \    | \    / \ |
    |vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv|
    |                                                                              |
    |                       URNA DO SARCÓFAGO DE HATSHEPUT                         |
    |                                                                              |
    |     _                                                                  _     |
    |    /_\                                                                /_\    |
    |    =|=                                                                =|=    |
    |               .*.                                          .*.               |
    |              ;(;);________________________________________;(;);              |
    |              |;;;    _    _         _    _        _    _   ;;;|              |
    |              | ;/}    \/}/     /}    \/}/     /}   \/}/    /; |              |
    |              |_/|\_    |_    _/|\_    |_    _/|\_   |_   _/|\_|              |
    |              | / \     | \    / \     | \    / \    | \   / \ |              |
    |            __|vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv|__            |
    |___________|______________________________________________________|__________lc
    ''')


    print('''
    Você chegou ao Sarcófago da Rainha Hatshepsut.
    Cobras e escorpiões o aguardam famintos!

    Atordoado você procura por Kaleo e ele não está aqui.

    Hatshepsut amaldiçoa qualquer homem que ouse entrar neste lugar.
    Porém você terá uma chance de escapar.
    A serpente de Hatshepsut comandará o ataque se você não acertar a charada.
    ''')

    charada2 = '''
    Descubra a palavra:

    > letra que é número
    > parece um sapo, mas não é
    > na ordem inversa do som é a sexta
    > segunda palavra na sequência do oposto do antônimo de "me entregue"

    Dica: O que você procura, nela não está.\n
    '''
    
    print(charada2)

    respostaCharada2 = input("Digite sua resposta: ")

    if respostaCharada2.lower() == "pirâmide":
        print("Você acertou! Vá para o Templo de Karnak.\n")
    else:
        print("Você errou. Será atacado pelas serpentes e escorpiões. FIM DE JOGO.\r\n")
        # repetirJogo3 = input("Deseja jogar novamente? [S / N]")
        # if repetirJogo3.upper() == "S":
        #     jogar()
        # else:
        #     print("Até a próxima!")


    print('''
    Você chegou ao Templo de Karnak. 
    Subirá 3 lances de escadas, atravessará uma alameda, e chegará ao Salão sem Fim.
    ''') 

    print('''
    Aqui é possível ouvir gargalhadas e gritos, mas você está confuso e não consegue saber de onde vem cada som, 
    nem há quanto tempo os escuta. 

    Dentro desta sala o tempo e o espaço estão distorcidos.
    A sala muda de tamanho a cada 5 minutos.
    E o ritmo das horas é alterado a cada 3 minutos, podendo ir para o futuro 
    ou para o passado, aleatoriamente.
    ''')

    print('''
    Você sabe que está perto de encontrar Kaleo.
    Corra o mais rápido possível para não ficar preso eternamente.

    Escolha seu destino:
    1. Corredor das Múmias 
    ou
    2. Sala dos Rubis
    ''')

    corredorMumias = 1
    salaRubis = 2
    enigma1 = '''
    Enigma:
    Em qual alternativa há três oitos, três zero?
    a) 88830
    b) 3830
    c) 888000
    d) 383000\n
    '''
    
    charada3 = "Charada:\nOcorre uma vez a cada minuto,\nduas vezes a cada momento,\nmas jamais a cada quinhentos anos."

    print('''
         __w
                 ,%%%%
                .%%%_/  ,_
                %%/(___//
                %%||))-'
              ,%%%)\(
              %%%/ \\
              ,%%\  ;
                % | |
                  | |
                 /  |
         jgs    /___|
         ''')

    cena2 = int(input("Digite o número do local escolhido [1 / 2]: "))

    if cena2 == corredorMumias:
        print("Bem-vindo ao Corredor das Múmias!\n")
        print('''
        Kaleo será mumificado vivo.
        Foi atraído pelos encantos de Cleópatra, mas foi confundido com um saqueador e caiu 
        nas garras das 12 múmias que protegem o tesouro da Faraó.
        As 12 múmias famintas começam a correr em sua direção.
        Decifre o enigma para imobilizá-las.\n
        ''')
        print(enigma1)
        respostaEnigma1 = input("Digite sua resposta: ")
        if respostaEnigma1.lower() == "a":
            print("Resposta certa! Parabéns você escapou da Maldição da Rainha!!!\r\n")
        else:
            print("Resposta errada. Você caiu na maldição da Rainha! FIM DE JOGO.\r\n")
        #     repetirJogo4 = input("Deseja jogar novamente? [S / N]")
        # if repetirJogo4.upper() == "S":
        #     jogar()
        # else:
        #     print("Até a próxima!")
    elif cena2 == salaRubis:
        print("Bem-vindo a Sala dos Rubis!\n")
        print('''
        Kaleo, está enfeitiçado por Cleópatra.
        A Faraó gargalha pois sabe que está perto de aprisionar vocês para sempre!
        Sentada em um trono de ouro ela está com o pé direito sobre a cabeça de Kaleo e assim a mente dele
        fica cada vez mais devotada à Rainha e distante da realidade.
        Para libertá-lo da maldição, responda a charada.
        \n''')

        print(charada3)

        respostaCharada3 = input("Digite sua resposta: \n")

        if respostaCharada3.lower() == "m":
            print("Use moeda com a face de Cleopatra. Ela é a chave para sair da Sala dos Rubis.\r\n")
            print("Resposta correta! Parabéns você escapou da maldição da Rainha!!!\n")
        else:
            print("Resposta errada. Agora você também será enfeitiçado. Você caiu na Maldição da Rainha!!!\r\n")
        #     repetirJogo5 = input("Deseja jogar novamente? [S / N]")

        # if repetirJogo5.upper() == "S":
        #     jogar()
        # else:
        #     print("Até a próxima!")


    print('''
                                     \  /
                                    (())
                                    ,~L_
                                   2~~ <\ 
                                   )>-\y(((GSSSSSSssssss>=  _/
 ___________________________________)v_\__________________________________
(_// / / / (///////\3__________((_/      _((__________E/\\\\\\\\\) \ \ \ \ \ \_)
  (_/ / / / (////////////////////(c  (c /|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\)\ \ \ \ \_)
    "(_/ / / /(/(/(/(/(/(/(/(/(/(/\_    /\)\)\)\)\)\)\)\)\)\)\ \ \ \_)"
       "(_/ / / / / / / / / / / / /|___/\ \ \ \ \ \ \ \ \ \ \ \ \_)"
 jjs      "(_(_(_(_(_(_(_(_(_(_(_(_[_]_|_)_)_)_)_)_)_)_)_)_)_)_)"
                                   |    \ 
                                  /      |
                                 / /    /___
                                /           "~~~~~__
                                \_\_______________\_"_?
''')


    print("-="*15)
    print("|        FIM DE JOGO       |".center(30))
    print("-="*15)

jogarMortalQueen()

novaRodada = int(input('''Deseja jogar novamente?
    (1) - Sim
    (2) - Não\n'''))

if (novaRodada == 1):
    jogarMortalQueen()
else:
    print("ATÉ A PRÓXIMA!")
