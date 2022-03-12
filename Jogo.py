import random

(print('#' * 46)
(print('Estudante: Thatiane F Ribas'))
(print ('regras'))
(print ('- * 46'))

#número de jogadores começa com 0
num_jogadores = 0
while num_jogadores <2:
    num_jogadores = int(input('Informe a quantidade de jogadores:'))
    if num_jogadores <2:
        print('Número invalido. Você precisa de no minimo 2 jogadores!')

#nome dos jogadores
lista_jogadores = [ ]
for i in range (num_jogadores)
    nome = str(input('Informe o nome do jogador' + str(i + 1) + ': ')).strip()
    lista_jogadores.append(nome)

#iniciar o jogo
print('Prontos para começar?')
str(input('Digite S para iniciar:')).strip() .upper()

#configurações dados
dado_verde = "CCCEPP"
dado_amarelo = "CCEEPP"
dado_vermelho = "CEEEPP"
copo_dados = [dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_amarelo, dado_amarelo, dado_amarelo, dado_amarelo, dado_vermelho,dado_vermelho,dado_vermelho]
dados_sorteados = []
jogador_atual = 0
cerebros = 0
espingardas = 0
pegadas = 0

#sorteio de dados
while true:
    print('Turno do Jogador { }' .format(lista_jogadores [jogador_atual]))
    print('_' * 36)
    for i in range(0,3,1)
        num_sorteado = random.randint(0,12)
        dado_sorteado = copo_dados [num_sorteado]
        if dado_sorteado == "CCCEPP"
            cor_dado = "Verde"
        elif dado_sorteado == "CCEEPP"
            cor_dado = "Amarelo"
        else
            cor_dado = "Vermelho"
        print('A cor do dado é:' {} .format(cor_dado))
        dados_sorteados.append(dados_sorteados)

print('Vamos ver as faces')
str(input('Digite S para iniciar:')).strip() .upper()
print('as faces são:')

for i in range (0,3,1)
    face_sorteada = random.choice(dados_sorteados)
    if face_sorteada == C
        print('Cérebro!')
        cerebros = cerebros + 1
    elif face_sorteada == E
        print('Vc levou um tiro')
        espingardas = espingardas +1
    else
        print(pegada)
        pegadas = pegadas +1

#TERMINAR
print(Pontuação atual)
print('-' * 30)
print('Vamos continuar?')
str(input('Digite S para iniciar:')).strip() .upper()

continuar_turno = str(input('Continuar? s ou n')).strip() .upper()

    if continuar_turno == "n"
        jogador_atual= jogador_atual +1
        dados_sorteados = []
        espingardas = 0
        cerebros = 0
        pegadas = 0
        if jogador_atual == len(lista_jogadores)
            print('Fim do jogo')
            break
        else:
            print('Iniciando novamente')
            dados_sorteados = []


