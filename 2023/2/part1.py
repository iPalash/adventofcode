import sys
filename = sys.argv[1]

def read_game(line):
    game, data = line.split(":")
    game_num = int(game.split(" ")[-1])
    sets = map(lambda x:x.strip(), data.split(";"))
    sets_data = []
    for set in sets:
        picked = map(lambda y:y.strip(), set.split(","))
        balls = {}
        for p in picked:
            num, color = map(lambda y:y.strip(),p.split(" "))
            balls[color] = int(num)
        sets_data.append(balls)
    return game_num, sets_data

total = {"red":12 , "green":13, "blue":14}

def game_valid(game):
    for set in game:
        for key,val  in set.items():
            if total[key]<val:
                return False
    return True

with open(filename, 'r') as f:
    lines = f.readlines()
    sm = 0
    for line in lines:
        idx, sets = read_game(line)
        if game_valid(sets):
            sm+=idx
    print(sm)