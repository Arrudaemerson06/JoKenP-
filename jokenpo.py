from time import sleep
import emoji
from random import randint
# acumuladores
placarpc = placarp1 = 0
# emojis
pedra = emoji.emojize(':left-facing_fist:')
papel = emoji.emojize(':raised_hand:')
tesoura = emoji.emojize(':crossed_fingers:')
itens = pedra, papel, tesoura
# inicio do jogo
nome = str(input('Qual é o seu nome? ')).strip().title()
while True:
    print(f"""Bem vindo ao Jokenpô {nome}
    Suas opções são:
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura
    [ 9 ] Ver o Placar""")
    jogador = int(input('Qual a sua jogada? '))
    computador = randint(0, 2)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    sleep(1)
    print('-=' * 10)
    print('O computador jogou {}'.format(itens[computador]))
    print('Você jogou {}'.format(itens[jogador]))
    print('-=' * 10)
    if computador == 0:
        if jogador == 0:
            print('EMPATE')
            placarpc += 1
            placarp1 += 1
        elif jogador == 1:
            print('JOGADOR VENCE')
            placarp1 += 1
        elif jogador == 2:
            print('COMPUTADOR VENCE')
            placarpc += 1
        else:
            print('Jogada inválida.')
    if computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCE')
            placarpc += 1
        elif jogador == 1:
            print('EMPATE')
            placarpc += 1
            placarp1 += 1
        elif jogador == 2:
            print('JOGADOR VENCE')
            placarp1 += 1
        else:
            print('Jogada inválida.')
    if computador == 2:
        if jogador == 0:
            print('JOGADOR VENCE')
            placarp1 += 1
        elif jogador == 1:
            print('COMPUTADOR VENCE')
            placarpc += 1
        elif jogador == 2:
            print('EMPATE')
            placarpc += 1
            placarp1 += 1
        else:
            print('Jogada inválida.')
    opc = str(input('Deseja jogar de novo? [S/N] ')).strip().upper()
    if opc in 'N':
        break
print(f"""O placar final foi:
{placarpc} pontos para o Computador
{placarp1} pontos para {nome}""")
if placarpc > placarp1:
    print('COMPUTADOR VENCEU!!')
elif placarpc < placarp1:
    print(f'{nome} VENCEU!!!')
else:
    print('EMPATE!!')
