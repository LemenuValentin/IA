#librairie IA
import random

def ChooseAssassins(state):
    Villagers = []
    for i in range(10):
        for j in range(10):
            if state['people'][i][j] not in {'knight','king',None}:
                    Villagers.append(state['people'][i][j])
    Assassins = []
    while len(Assassins)!=3:
        who = random.choice(Villagers)
        if who not in Assassins:
            Assassins.append(who)
    return Assassins

#def MoveVillagers(state):
    #PAvillagers = state['CARDS'][
