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


def fewest_cubes_power(game):
    fewest = {"blue":0,"green":0, "red":0} # let's assume zero min for now
    for set in game:
        for key,val  in set.items():
            if val>fewest[key]:
                fewest[key]=val
    pw = 1
    for val in fewest.values():
        pw*=val
    return pw

with open(filename, 'r') as f:
    lines = f.readlines()
    sm = 0
    for line in lines:
        idx, sets = read_game(line)
        sm += fewest_cubes_power(sets)
    print(sm)