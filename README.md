# PROJETO 1 - VAMO AI - JOGO EM PYTHON :snake:


## Visão geral do projeto: :crystal_ball: 

## O que é preciso para jogar?
Você precisa apenas ter o python instalado na sua máquina.     
Não há necessidade de instalação de bibliotecas adicionais.      
Pode rodar o jogo no terminal, pode executar também no Visual Studio Code ou outra IDE de sua preferência.       

Para rodar no terminal, siga para o diretório onde está o arquivo .py       
Use o comando:
```
python projeto1JogoMortalQueen.py
``` 
<br>   

#### O objetivo foi fazer um jogo com vários finais baseados em escolhas, seguindo este fluxo padrão:

1. Mostrar o texto explicando o cenário atual 
2. Fornecer opções de tomada de decisão 
3. Receber a escolha da pessoa usuária 
4. Se for um final de jogo, mostrar mensagem de fim de jogo (venceu, ganhou etc) e mostrar pelo menos uma única opção, que é a de jogar novamente 
5. Se não, voltar para o primeiro passo. Utilize o print para mostrar escolhas ou dados para a pessoa jogadora;
   Utilize o prompt de comando para pegar dados da pessoa jogadora;
6. A história do jogo precisa ter:
   1. Um tema específico
   2. Enredo
   3. Título
   4. Locais diferentes (pelo menos 3)
   5. Personagens diferentes (pelo menos 3)
   6. Condições de vitória (pelo menos 2)
   7. Condições de derrota (pelo menos 4)


---



### Meu Grupo: :white_check_mark:

- Inajá
- Lis
- Demétrio
- Olavo

---



### Meu jogo: MORTAL QUEEN :crown:  

![](https://www.imagensanimadas.com/data/media/37/egito-imagem-animada-0040.gif)



- Tema: Egito
- O jogador poderá escolher entre 3 personagens: Joanna, Luan ou Hannah.
  - Joanna é curiosa, pratica escalada e não perde a oportunidade de desvendar um mistério.
  - Luan é bom em raciocinar rápido, nada bem e corre como um guepardo.
  - Hannah é observadora, muito corajosa e contorcionista em um circo famoso.
- Locais: Pirâmides de Gizé, Templo de Karnak, Salão sem Fim, Corredor das Múmias e Sala dos Rubis.
- Condições de vitória (mínimo 2): Se resolver o enigma no Corredor das Múmias ou se resolver a charada na Sala dos Rubis.
- Condições de derrota (mínimo 4):  Se não acertar a charada 1 na pirâmide Quéops. Se não acertar a charada 2 na pirâmide Quéops. Se errar o enigma no Corredor das Múmias ou se errar a charada na Sala dos Rubis. 
- Fluxograma do jogo:

![](https://github.com/michelle-lira/jogoResilia/blob/main/imagensMortalQueen/organogMortalQueen.png)



---



### Roteiro: :page_with_curl:  

A proposta para a construção deste programa foi desenvolver um programa simples e divertido, com recursos básicos do python aprendidos no primeiro módulo do VamoAI, a formação Analista de Dados, da Resília Educação em parceria com o Ifood. O enredo foi pensado para envolver suspense, aventura e raciocínio lógico, utilizando charadas e enigmas para determinar o avanço ou não da trama. O contexto também envolve duas maldições uma lançada sobre o Cairo por Hatshepsut e Cleópatra. 

Hatshepsut é uma das mais poderosa e mais bem sucedidas mulheres de toda a história egípcia. O país prosperou sob o seu reinado, com expansão do comércio e campanhas militares. Também ficou famosa pelos grandiosos monumentos que mandou construir e por algumas adições ao Templo de Karnak. No contexto do jogo, Hatshepsut teria lançado uma maldição e qualquer homem que ousasse entrar nas dependências onde ficam seu sarcófago e seu tesouro.



![](https://cdna.artstation.com/p/assets/images/images/031/445/436/large/brian-cramer-egyptian-tomb3-rgb.jpg?1603658559)



Já Cleópatra, foi a pessoa mais rica do Mediterrâneo. E também articulada, carismática, fluente em nove línguas, versada em  política, diplomacia e governo, estrategista militar. Dona de um grande  senso de humor e de muito charme. Conquistava quem quisesse. No jogo, a maldição de Cleópatra era aprisionar para sempre a mente daquele que cedesse aos seus encantos e adentrasse aos seus aposentos. Já aos que tentassem roubar seu tesouro, deixou 12 ferozes múmias à espreita.



![](https://1.bp.blogspot.com/-UnGuJwuXQ_Y/XQPt1ql8YkI/AAAAAAAA_Qs/8r0EjPU4mMM0nwF6nGXfTOyNWl5y-J4LQCLcBGAs/s1600/Cleopatra.jpg)



Na história, em viagem ao Egito, Kaleo, desaparece. A ideia é que o jogador escolha um, entre três personagens (Joanna, Luan ou Hannah) para investigar o sumiço de Kaleo e salvá-lo. O personagem escolhido conseguirá algumas pistas que apontarão para Hatshepsut e para Cleópatra. Duas poderosas e intrigantes Rainhas do Egito.

A aventura começa em uma das Pirâmides de Gizé, a Quéops. Através de charadas e enigmas o jogo segue pelo Salão das Pinturas e pelo Sarcófago de Hatshepsut, ambos dentro da Pirâmide.
O Salão das Pinturas é um organismo vivo. As paredes estão cheias de pinturas de Reis, Rainhas, trabalhadores, artesãos e famílias inteiras com suas rotinas, crenças e paixões. Elas comandam o solo de areia movediça para proteger os tesouros escondidos na pirâmide.
Na urna do sarcófago, a serpente de Hatshepsut comandará o ataque caso o jogador não acerte a charada. 



![](https://images.memphistours.com/large/3f46543f340fca6d19d744adde6569cc.jpg)



Em seguida é a vez do Templo de Karnak, com o Salão sem Fim:

> É possível ouvir gargalhadas e gritos, mas você está confuso e não consegue saber de onde vem cada som, 
> nem há quanto tempo os escuta. 

Dentro desta sala o tempo e o espaço estão distorcidos. A sala muda de tamanho e a contagem do tempo se altera constantemente. O destino daquele que não conseguir sair de lá é perder-se para sempre no fluxo do tempo.
Aos que superarem os artifícios do salão é permitido escolher o próximo e último destino:
O corredor das múmias ou A sala dos rubis.

---



### Final 1️⃣: ⚜️

Corredor das Múmias.
Aqui as 12 múmias que protegem o tesouro da Faraó Cleópatra entrarão em ação.
Será preciso decifrar o enigma para imobilizá-las.

Se Kaleo estiver sob o poder das 12 múmias e for salvo, o jogador vence!

---



### Final 2️⃣: :gem:

Sala dos Rubis.

Aqui a Rainha descansa e também aprisiona os seus eternos apaixonados.

Se Kaleo estiver enredado nos artifícios de Cleópatra, dificilmente sairá!

---



## Estrutura de códigos:

Os códigos do jogo são simples e neste projeto foi permitido apenas a implementação dos conteúdos introdutórios, estudados no primeiro módulo da formação Analista de Dados, da Resília Educação.

Manipulação de strings, formatações básicas, funções built-in do Python e criação de funções dentro do programas foram permitidos, bem como condicionais e laços de repetição.

Segue abaixo um exemplo:

```
while jogadorEscolhido != 1 and jogadorEscolhido != 2 and jogadorEscolhido != 3:
    print("Digite um número de 1 a 3. Tente novamente.\n")
    jogadorEscolhido = int(input("Com quem você deseja jogar? Digite 1 / 2 / 3: \n"))
    if jogadorEscolhido == 1:
        print("Olá, Joanna! Prepare-se para começar a aventura!\n")
        break
    elif jogadorEscolhido == 2:
        print("Olá, Luan! Prepare-se para começar a aventura!\n")
        break
    elif jogadorEscolhido == 3:
        print("Olá Hannah! Prepare-se para começar a aventura!\n")
        break
```



---



## Links úteis: :link:



* https://www.ancient.eu/trans/pt/2-1040/as-grandes-soberanas-do-antigo-egito/
* https://www.bbc.com/portuguese/geral-54244549![]()
* https://aventurasnahistoria.uol.com.br/noticias/reportagem/morte-de-cleopatra-ultima-farao.phtml

* http://matematicosdemogi.blogspot.com/2016/07/os-papiros-da-matematica-egipcia-rhind.html
* https://docs.python.org/pt-br/3/library/functions.html
* https://www.asciiart.eu/art-and-design/egyptian
* https://ascii.co.uk/art/sphinx





