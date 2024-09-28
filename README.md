Teste de habilidade para estágio na empresa Target Sistemas.

Prova Técnica:

1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


RESPOSTA: Programa com nome target1.fibonacci postado neste repositório. A linguagem Python foi escolhida para este programa.




2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;


RESPOSTA: Programa com nome target2.letraA postado neste repositório. A linguagem Python foi escolhida para este programa.




3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?

RESPOSTA: SOMA = 77


4) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, (9)  # soma 2 ao anterior

b) 2, 4, 8, 16, 32, 64, (128) # dobra o número anterior

c) 0, 1, 4, 9, 16, 25, 36, (49) # soma ao anterior o número ímpar da sequência crescente 1,3,5,7,9,11,13

d) 4, 16, 36, 64, (100) # soma ao anterior a sequência crescente 12, 20, 28, 36 {soma-se 8 à diferença do número com seu anterio}

e) 1, 1, 2, 3, 5, 8, (13) # soma do número com seu anterior

f) 2,10, 12, 16, 17, 18, 19, (200) # números inteiros que começam com a letra D


5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

RESPOSTA: Essa questão deve ser resolvida em 2 passos. 
Passo 1: Ligar o primeiro interruptor, esperar alguns minutos, desligar o interruptor. Em seguida, ligar o segundo interruptor e ir até a primeira sala. Caso a lâmpada esteja acesa, o segundo interruptor está concetado nesta sala, caso a lâmpada esteja apagada, porém quente, o primeiro interruptor está ligado nesta sala, caso a lâmpada esteja apagada e fria, o terceiro interruptor está ligado nesta sala. Assim, saberemos qual interruptor está ligado nesta sala, e já podemos descobrir o da próxima sala. 
Passo 2: Sobrou apenas 2 interruptores e 2 salas após o passo 1, portanto, liga-se um dos interruptores e vá para próxima sala. Caso a lâmpada esteja acesa, o interruptor ligado está concetado nesta sala, caso a lâmpada esteja apagada, o interruotor não ligado está concetado nesta sala. Assim, descobrimos qual interruptor está conectado nesta sala, sobrando apenas um interruptor para a última sala.


Obrigada pela visita!
