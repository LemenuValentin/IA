#librairie IA
import random

#prend 3 assassins aléatoirement
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

#retrouve les coordonnées d'un citoyen
def coord(name,state):
    for y in range(10):
        for x in range(10):
            if state['people'][y][x] == str(name):
                return y,x
            
#regarde si on est sur un toit ou non
def OnRoof(x,y,Newx,Newy,state):
    if state['board'][x][y] == 'G' and state['board'][Newx][Newy] == 'R':
        return True
    
#donne les coordonnées de la position après déplacement
def nextposfree(x,y,direction,state):
    if direction == 'N':
        if x != 0:
            x = x-1
    if direction == 'S':
        if x != 9:
            x = x+1
    if direction == 'E':
        if y != 9:
            y = y+1
    if direction == 'W':
        if y != 0:
            y = y-1
    return x,y
