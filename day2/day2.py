import numpy as np

#Part 1
valid_games = []
with open("input.txt") as infile:
    for line in infile:
        game_id, sets = line.split(':')[0].split(' ')[-1], line.split(':')[-1].split(';')
        max_matrix = np.array([12,13,14]*len(sets)).reshape(len(sets),3)
        games_vec = np.zeros(3*len(sets))
        for i,game in enumerate(sets):
            k = i*3
            for dice in game.split(','):
                if 'red' in dice:
                    games_vec[k] = int(dice.split('red')[0])
                elif 'green' in dice:
                    games_vec[k+1] = int(dice.split('green')[0])
                elif 'blue' in dice:
                    games_vec[k+2] = int(dice.split('blue')[0])

        check = games_vec.reshape(len(sets),3) > max_matrix
        if check.sum() == 0:
            valid_games += [game_id]
print(sum([int(x) for x in valid_games]))

#Part 2
powers = []
with open("input.txt") as infile:
    for line in infile:
        game_id, sets = line.split(':')[0].split(' ')[-1], line.split(':')[-1].split(';')
        games_vec = np.zeros(3*len(sets))
        for i,game in enumerate(sets):
            k = i*3
            for dice in game.split(','):
                if 'red' in dice:
                    games_vec[k] = int(dice.split('red')[0])
                elif 'green' in dice:
                    games_vec[k+1] = int(dice.split('green')[0])
                elif 'blue' in dice:
                    games_vec[k+2] = int(dice.split('blue')[0])

        games_matrix = games_vec.reshape(len(sets),3)
        max_by_color = games_matrix.max(axis=0)
        powers += [np.prod(max_by_color)]
print(sum(powers))