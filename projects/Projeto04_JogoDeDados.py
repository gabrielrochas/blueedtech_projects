# Utilizando os conceitos aprendidos até dicionários, crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios.
# O programa tem que:
# • Perguntar quantas rodadas você quer fazer;
# • Guardar os resultados dos dados em um dicionário.
# • Ordenar este dicionário, sabendo que o vencedor tirou o maior número no dado.
# • Mostrar no final qual jogador ganhou mais rodadas e foi o grande campeão.
#!pip install art 
from art import *
from random import randrange
from time import sleep
import os

os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal
tprint(f'Vamos rolar dados?')
sleep(2)
os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal

players = {} # Dictionary of players
winners = [] # List of winners

loading = ['3','2','1']
# Do until user enter a integer number
while True:
    rounds = input('Digite o número de rodadas: ')
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal
    # Check if the user enter a integer.
    if int(rounds.isnumeric()) == True:
        # Check if user realy want to play more then 10 rounds
        if int(rounds) > 10:
            check = input(f'Tem certeza que quer jogar {rounds} rodadas?:[Sim ou Não] ').strip().lower()[0]
            if check not in 'sn':
                print('Opção inválida. Tente novamente.')
            # If doesn't return to start
            elif check == 'n':
                continue
            else:
                break
        # Ends rounds block check
        break
    else:
        print('Você precisa digitar um número')
        continue
    # Ends integer block check
diceValues = ['⚀','⚁','⚂','⚃','⚄','⚅']
for x in range(0, int(rounds)):
    tprint(f'Rodada {x+1}')
    majorValue = 0
    # Roll dice for each player and assign a value to each one
    for i in range(1,5):
        players['Jogador '+str(i)] = randrange(6)
    # Print players and the dice value that each one have
    for key, value in players.items():
        print(f'{key} - tirou {value+1}: {diceValues[value]}')
        sleep(0.5)
        # Check who wins
        if majorValue < value:
            majorValue = value
            winner = key
        elif value == majorValue:
            winner = '0'
    # List of all winners
    if winner != '0':
        winners.append(winner)
    sleep(1)
    # Print whin the round
    if winner != '0':
        tprint(f'Vencedor: {winner}', font='small')
    else:
        tprint('Rodada empatada', font='small')
    # Loading... 
    sleep(2) 
    for i in loading: tprint(i, font='small'), sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal
del i, key, majorValue, rounds, value, winner, x
# Create a dict of winners sortered by player [key]
dictWinner = {i: winners.count(i) for i in sorted(winners)}
# Generate a list of tuples and ordering the dictWinner by value
orderWinnerValue = sorted(dictWinner.items(), key=lambda v: v[1], reverse=True)
# Max rounds a player could have won
check = len(dictWinner)
num = 0
greatWinner = {}
for i in orderWinnerValue:
    if check != i[1] and num < i[1]: 
        check = i[1]
    if check == i[1]:
        victory = 'Vitoria' if i[1] == 1 else "Vitorias"
        greatWinner[i[0]] = i[1]
        num = check
        print(f'{i[0]} teve {i[1]} {victory}')

# If match was draw, ask if use want play tiebrake
del orderWinnerValue
greatWinner = {'Jogador 1': 2, 'Jogador 3':2}
if len(greatWinner) > 1:
    master = {};
    check = len(greatWinner)
    num = 0
    # Check if user want to play tiebrake
    while True:
        if len(greatWinner) > 1 or len(master) != 1:
            tieBrake = input('Partida empatada.\nDeseja jogar partida desempate?\nSim ou Não: ').strip().lower()[0]
        # In afirmative case
        if tieBrake == 's':
            diceValue = 0
            majorValue = 0
            winners = []
            # Generate new dice values
            for key, value in greatWinner.items():
                value = randrange(6)
                master[key] = value
                print(f'{key} - {diceValues[value]}')
                # Check who wins
                if majorValue < value:
                    majorValue = value
                    winner = key
                elif value == majorValue:
                    winner = '0'
            # List of all winners
                if winner != '0':
                    winners.append(winner)
            sleep(0.5)
            # Print the great champion
            if winner != '0':
                tprint(f'Grande Campeão: {winner}')
                break
            else:
                tprint('Houve um empate nessa rodada')
                # Loading... 
                sleep(2) 
                for i in loading: tprint(i, font='small'), sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal
                continue
        # else the break check block
        else:
            break

else:
    for k, v in greatWinner.items():
        tprint(f'\nGrande campeao\n{k}\nGanhou {v} partidas!')