from pwn import remote


P = 36583
r = remote('202.38.69.223', 10006)

def receiveMap():
    while True:
        alien_pos = r.recvline().decode()
        if alien_pos.startswith('Your'):
            pos = eval(alien_pos.split(':')[-1].strip())
            Ship = pos
            break            
    Alien = []
    while True:
        alien_pos = r.recvline().decode()
        if alien_pos.startswith('Alien'):
            pos = eval(alien_pos.split(':')[-1].strip())
            Alien.append(pos)
        else:
            break
    return Ship, Alien

def getSeed(pre, nxt):
    direction_choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    seed = 0
    shift = 0
    for a, b in zip(pre, nxt):
        which = direction_choices.index((b[0] - a[0], b[1] - a[1]))
        seed |= which << shift
        shift += 2
    return seed

def moveOnce(alienMap, seed):
    direction_choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(8):
        direction = direction_choices[(seed >> i * 2) & 3]
        x = alienMap[i][0] + direction[0]
        y = alienMap[i][1] + direction[1]
        alienMap[i] = (max(min(x, 30), 1), max(min(y, 30), 1))
    return alienMap

def predictAlien(alienMap, seed, mask, cnt):
    mapList = []
    for _ in range(cnt):
        seed = seed * mask % P
        alienMap = moveOnce(alienMap[:], seed)
        mapList.append(alienMap)
    return mapList

mp = []
for i in range(4):
    mp.append(receiveMap())
    if i != 3:
        r.sendline()
seeds = [getSeed(mp[i][1], mp[i + 1][1]) for i in range(3)]
mask = seeds[1] * pow(seeds[0], P - 2, P) % P
print('mask:', mask)
assert seeds[1] * mask % P == seeds[2]

alien_predict = predictAlien(mp[-1][1], seeds[-1], mask, 256)
die = [[] for _ in range(256)]
for i in range(256):
    for c in range(8):
        dist = 30 - alien_predict[i][c][0]
        shoot_time = i - dist
        die[shoot_time].append((alien_predict[i][c][1], c))
pos = 15
curTime = -1
shooted = 0
alien_alive = [True for i in range(8)]
for i in range(256):
    for x, c in die[i]:
        if alien_alive[c] and i - curTime > abs(x - pos):
            steps = i - curTime
            curTime = i
            alien_alive[c] = False
            for _ in range(x - pos):
                r.sendline(b'D')
            for _ in range(pos - x):
                r.sendline(b'A')
            for _ in range(steps - abs(x - pos) - 1):
                r.sendline()
            r.sendline(b'S')
            pos = x
            shooted += 1
            if shooted == 8:
                r.interactive()