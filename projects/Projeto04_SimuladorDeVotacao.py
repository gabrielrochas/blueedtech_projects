# Projeto 04 - Simulador de votação:
# Crie um programa que simule um sistema de votação, ele deve receber votes até
# que o usuário diga que não tem mais ninguém para votar, esse programa precisa ter
# duas funções:
# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o
# ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um
# valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.
# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá
# da função autoriza_voto()) e o voto que é o número que a pessoa votou.
# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o
# contrário a 2° função deve validar o número que a pessoa escolheu, ela pode
# escolher de 1 a 5 (crie 3 candidatos para a votação):
# ● 1, 2 ou 3 - Votes para os respectivos candidatos
# ● 4- Voto Nulo
# ● 5 - Voto em Branco
# Sua função votacao() tem que calcular e mostrar:
# ● O total de votes para cada candidato;
# ● O total de votes nulos;
# ● O total de votes em branco;
# ● Qual candidato venceu a votação

import os
import tabulate  # Format the list in tables. Run in terminal --> pip install tabulate
from art import *
from time import sleep
from random import randint

votation = []   #GLOBAL LIST
allVotes = []   #GLOBAL LIST
validVotes = [] #GLOBAL LIST
elected = []    #GLOBA LIST

# Method to autorize vote.
# Here, in Brazil, vote is mandatory for people between 18 and 70 years old. Optional to that over 16 and under 18 years and above 70. And that under 16 years can't vote at all
def autoriza_voto(age):
    if 16 < age < 18 or age > 70:
        vote = 'OPCIONAL'
    elif age < 16:
        vote = 'NEGADO'
    else:
        vote = 'OBRIGATORIO'

    return f'{vote}'

#
def votacao(authorization = ' ', votedNumber = ' '):
    from tabulate import tabulate
    
    if authorization == 'NEGADO':
        return f'Voce não pode votar'
    else:
        if authorization == ' ' and votedNumber == ' ':
            clear()
            tprint('Processo de votação encerrado')
            sleep(2)
            clear()

            allVts, valVts, elctd = finalCount()
            headers = ['Candidato', 'Número', 'Votos Recebidos']

            print('Todos os votos:')
            print(tabulate(allVts, headers, tablefmt='grid'))
            
            print('Votos validos:')
            print(tabulate(valVts, headers, tablefmt='grid'))
            
            print('Eleito:')
            print(tabulate(elected, headers, tablefmt='grid'))
        # return True

# Count votes
def countVotes(vote):
    global votation

    for k, v in enumerate(names):
        if v['num'] == vote:
            v['votes'] += 1
            votation.append(v['name'])

# Generate two list: validVotes and elected
def finalCount():
    # global allVotes, validVotes, elected
    valVts = []
    for k, v in enumerate(names):
        for i in votation:
            if i == v['name']:
                v['votes'] += 1
        # Count all votes
        allVotes.append(list(v.values()))
        # Count valid votes
        if 'Nulo' != v['name'] != 'Branco':
            validVotes.append(list(v.values()))

    elct = 0
    for k in validVotes:
        for v in k:
            if elct <= k[2]:
                if elct != k[2]:
                    elected.clear()
                elected.append(k)
                elect = k[2]
                break
            else:
                break

    return allVotes, validVotes, elected

# Enter a person and check if can vote or not
def person():
    from datetime import date
    from names import get_first_name
    while True:
        while True:
            # name = input('Digite o seu nome: ')]
            name = get_first_name()
            if name.isnumeric() or len(name) < 1:
                print('Nome inválido. Tente novamente.')
            else:
                checkName = True
                break
        # Check if the user enter a valid year
        while True:
            currentYear = date.today().year 
            # birthYear = input('Digite o seu ano de nascimento [ex: 1985]: ')
            birthYear = str(randint(1900,2005))
            if birthYear.isnumeric():
                year = int(birthYear)                
                if 1900 < year < currentYear and (len(birthYear) == 4):
                    checkYear = True
                    break
                else:
                    print('Ano inválido. Tente novamente.')
            else:
                print('Ano inválido. Tente novamente.')
        # Exit while block
        if checkName and checkYear:
            break

    person = [name.title(), (currentYear - year)]
    clear()
    return person

# Start votation call person(), autoriza_voto() and votacao().
def startVotation(count):
    from playsound import playsound

    while True:
        votator = person()
        authorization = autoriza_voto(votator[1])
        if authorization == 'NEGADO':
            sleep(1)
            print(votacao(authorization=authorization))
        else:
            for k, v in enumerate(names):
                print(f'{k + 1} - {v["name"]}')

            # votatorChoice = input('\nDigite o seu voto: ').strip()[0]
            votatorChoice = str(randint(1,5))
            if not votatorChoice.isnumeric() or votatorChoice == '0':
                votateNumber = votacao(authorization, votedNumber = 4)
            elif votatorChoice in '12345':
                votateNumber = votacao(authorization, votatorChoice)
            playsound('./projects/vote_1.mp3')
            countVotes(int(votatorChoice))
            # sleep(1) 
            playsound('./projects/vote_2.mp3')
            clear()
        # os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
        tprint(f'FIM')
        sleep(0.5)
        clear()
        
        # endVotation = input('Deseja encerrar o processo de votação [S/N]: ').strip().lower()[0]
        count += 1
        if count == 10:
            endVotation = 's'
        else:
            endVotation = 'n'
        clear()
        if endVotation == 's':
            # call votacao() without values to end votation
            votacao()
            break

# Clear terminal
def clear():
    return os.system('cls' if os.name == 'nt' else 'clear') 
names = [
    {'name': 'Zazá', 'num': 1, 'votes': 0}, 
    {'name': 'Zezé', 'num': 2, 'votes': 0}, 
    {'name': 'Zizi', 'num': 3, 'votes': 0}, 
    {'name': 'Nulo', 'num': 4, 'votes': 0}, 
    {'name': 'Branco', 'num': 5, 'votes': 0}
    ]


# START VOTATION
# clear()
tprint('Bem vindo\nao Simulador de Urna Eletronica.', font='small')
# sleep(3)
clear()
startVotation(0)
