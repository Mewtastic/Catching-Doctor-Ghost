from pygame import math as pg
import random

print('''\n
      Thanks for playing Catching Doctor Ghost!\n
      The Rules are as follows:\n
      Each turn you pick a direction to move in.\n
      If you land on Dr. Ghost or he can't move, you Win.\n
      You don't know Dr. Ghost's position until every 4 turns.\n
      You can only move within the 26*26 grid.\n
      If you run out of turns, Dr. Ghost Wins.''')

GRID_SIZE = 26 # 0 - 25

N = pg.Vector2(0,1)
E = pg.Vector2(1,0)
S = pg.Vector2(0,-1)
W = pg.Vector2(-1,0)
NE = pg.Vector2(1,1)
SE = pg.Vector2(1,-1)
NW = pg.Vector2(-1,1)
SW = pg.Vector2(-1,-1)


grid = []
unvisited = []
first = True

player = pg.Vector2(0,0)
dr_ghost = pg.Vector2(random.randrange(15, 26), random.randrange(15, 26))

for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        grid.append(pg.Vector2(x,y))
        unvisited.append(pg.Vector2(x,y))

print('\n')
print('Enter your difficulty level 1-3')

level = input('level 1-3: ')

if level == '1':
    turns = 50
elif level == '2':
    turns = 40
else:
    turns = 30

print('Total Turns in Game: ' + str(turns))

TTIG = turns

def syscmd(message):
    print('*' + message + '*\n')

def check_neighbors(cell, grid):
    neighbors = []
    return_check = False
    if cell + N in grid:
        neighbors.append(cell + N)
        return_check = True
    if cell + NE in grid:
        neighbors.append(cell + NE)
        return_check = True
    if cell + E in grid:
        neighbors.append(cell + E)
        return_check = True
    if cell + SE in grid:
        neighbors.append(cell + SE)
        return_check = True
    if cell + S in grid:
        neighbors.append(cell + S)
        return_check = True
    if cell + SW in grid:
        neighbors.append(cell + SW)
        return_check = True
    if cell + W in grid:
        neighbors.append(cell + W)
        return_check = True
    if cell + NW in grid:
        neighbors.append(cell + NW)
        return_check = True

    if return_check:
        return neighbors
    else:
        return None

def check_player_movements(cell, grid):
    movements = []
    if cell + N in grid:
        north = 1
        movements.append(north)
    if cell + NE in grid:
        northeast = 2
        movements.append(northeast)
    if cell + E in grid:
        east = 3
        movements.append(east)
    if cell + SE in grid:
        southeast = 4
        movements.append(southeast)
    if cell + S in grid:
        south = 5
        movements.append(south)
    if cell + SW in grid:
        southwest = 6
        movements.append(southwest)
    if cell + W in grid:
        west = 7
        movements.append(west)
    if cell + NW in grid:
        northwest = 8
        movements.append(northwest)

    return movements

def ghosts_move(cell, neighbors):
    x = 0
    y = 0
    for i in neighbors:
        x += 1
    y = random.randrange(0, x)
    cell = neighbors[y]

    return cell

def player_movements(cell, movements):
    directions = []
    if 1 in movements:
        directions.append('North')
    if 2 in movements:
        directions.append('NorthEast')
    if 3 in movements:
        directions.append('East')
    if 4 in movements:
        directions.append('SouthEast')
    if 5 in movements:
        directions.append('South')
    if 6 in movements:
        directions.append('SouthWest')
    if 7 in movements:
        directions.append('West')
    if 8 in movements:
        directions.append('NorthWest')

    syscmd('Directions you can move: \n' + str(directions))
    syscmd('Choose your direction with the numberpad arrows\n 8 = North \n 9 = NorthEast \n 6 = East \n 3 = SouthEast \n 2 = South \n 1 = SouthWest \n 4 = West \n 7 = NorthWest \n 5 = Wait One Turn')
    direction = input('Direction: ')
    if direction == '8':
        if 'North' in directions:
            cell += N
        else:
            syscmd('You can\'t move there')
            player_movements(cell, movements)
    elif direction == '9':
        if 'NorthEast' in directions:
            cell += NE
        else:
            syscmd('You can\'t move there')
            player_movements(cell, movements)
    elif direction == '6':
        if 'East' in directions:
            cell += E
        else:
            syscmd('You can\'t move there')
            player_movements(cell, movements)
    elif direction == '3':
        if 'SouthEast' in directions:
            cell += SE
        else:
            syscmd('You can\'t move there')
            player_movements(cell, movements)
    elif direction == '2':
        if 'South' in directions:
            cell += S
        else:
            syscmd('You can\'t move there')
            player_movements(cell, movements)
    elif direction == '1':
        if 'SouthWest' in directions:
            cell += SW
        else:
            syscmd('You can\'t move there')
            player_movements(cell, movements)
    elif direction == '4':
        if 'West' in directions:
            cell += W
        else:
            syscmd('You can\'t move there')
            player_movements(cell, movements)
    elif direction == '7':
        if 'NorthWest' in directions:
            cell += NW
        else:
            syscmd('You can\'t move there')
            player_movements(cell, movements)
    elif direction == '5':
        cell = cell
        syscmd('You wait for Dr. Ghost to come to you')
    else:
        syscmd('Choose with the numbers given to you in the above list.')
        player_movements(cell, movements)

    print('')
    return cell


def gameLoop(turns, player, dr_ghost):
    end_game = False
    if turns != TTIG:
        syscmd('Turns left: ' + str(turns))
        print('')
        if turns % 4 == 0:
            syscmd('Breaking News! Dr. Ghost Sighted at ' + str(dr_ghost)
                   +('\n Suspect Likely Moved On, Police Investigate.'))
    if turns % 2:
        unvisited.remove(dr_ghost)
        ghost_neighbors = check_neighbors(dr_ghost, unvisited)
        if ghost_neighbors is not None:
            syscmd('The Dr. is moving...')
            dr_ghost = ghosts_move(dr_ghost, ghost_neighbors)
            if player == dr_ghost:
                syscmd('Breaking News! Dr. Ghost Captured at ' + str(dr_ghost)
                       +('\n Captured after daring chase down from Police.'))
                end_game = True
        else:
            syscmd('Breaking News! Dr. Ghost Captured at ' + str(dr_ghost)
               +('\n Captured after trapped for weeks authorities say.'))
            end_game = True
    else:
        syscmd('The Dr. makes no move')

    if not end_game:
        print('')
        syscmd('Time to Move, you\'re at ' + str(player))
        movements = check_player_movements(player, grid)
        player = player_movements(player, movements)
        if player == dr_ghost:
            syscmd('Breaking News! Dr. Ghost Captured at ' + str(dr_ghost)
                   +('\n Captured after daring chase down from Police.'))
        else:
            turns += -1
            if turns > 0:
                syscmd('[END TURN]')
                print('\n')
                gameLoop(turns, player, dr_ghost)
            else:
                syscmd('The Dr. Has Escaped!')


if first:
    first = False
    print('\n')
    gameLoop(turns, player, dr_ghost)
