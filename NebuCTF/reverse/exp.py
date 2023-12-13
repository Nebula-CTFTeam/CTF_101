import re

def read_postion(output_str):
    res = []
    pattern = r"\((\d+), (\d+)\)"
    matches = re.findall(pattern, output_str)
    for match in matches:
        res.append([int(match[0]), int(match[1])])
    return res

def get_direction(positions, positions_):
    return [(position[0] - position_[0], position[1] - position_[1]) 
            for (position, position_) in zip(positions, positions_)]

def get_seed(directions):
    res = 0
    for direction in directions[::-1]:
        idx = [(0, 1), (0, -1), (1, 0), (-1, 0)].index(direction)
        res += idx
        res <<= 2
    res >>= 2
    return res

def get_mask(seed0, seed1):
    for n in range(0xFFFF):
        if (n * seed0) % 36583 == seed1:
            return n

positions_str0 = '''
Alien0 position: (3, 5)
Alien1 position: (8, 8)
Alien2 position: (3, 11)
Alien3 position: (8, 14)
Alien4 position: (3, 17)
Alien5 position: (8, 20)
Alien6 position: (3, 23)
Alien7 position: (8, 26)
'''

positions_str1 = '''
Alien0 position: (3, 6)
Alien1 position: (8, 7)
Alien2 position: (4, 11)
Alien3 position: (8, 13)
Alien4 position: (3, 16)
Alien5 position: (8, 21)
Alien6 position: (2, 23)
Alien7 position: (7, 26)
'''

positions_str2 = '''
Alien0 position: (4, 6)
Alien1 position: (8, 8)
Alien2 position: (4, 12)
Alien3 position: (7, 13)
Alien4 position: (3, 17)
Alien5 position: (9, 21)
Alien6 position: (1, 23)
Alien7 position: (7, 27)
'''

positions0 = read_postion(positions_str0)
positions1 = read_postion(positions_str1)
positions2 = read_postion(positions_str2)

directions0 = get_direction(positions1, positions0)
directions1 = get_direction(positions2, positions1)

seed0 = get_seed(directions0)
seed1 = get_seed(directions1)

mask = get_mask(seed0, seed1)

print(seed0, mask)



