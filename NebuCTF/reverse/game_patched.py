import random

with open("flag", "r") as f:
    flag = f.read()

map_pattern = [
    ['+', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['+', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+']
]

class Ship:
    x: int
    y: int
    bullet_num: int = 8

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if (1 <= self.x + direction[0] <= 30):
            self.x += direction[0]
        if (1 <= self.y + direction[1] <= 30):
            self.y += direction[1]

class Bullet:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if (1 <= self.x + direction[0] <= 30):
            self.x += direction[0]
        if (1 <= self.y + direction[1] <= 30):
            self.y += direction[1]

class Alien:
    x: int
    y: int
    order: int

    def __init__(self, x, y, order):
        self.x = x
        self.y = y
        self.order = order

    def move(self, direction):
        if (1 <= self.x + direction[0] <= 30):
            self.x += direction[0]
        if (1 <= self.y + direction[1] <= 30):
            self.y += direction[1]
    
    def random_walk(self, seed):
        direction_choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        direction = direction_choices[(seed >> self.order * 2) & 3]
        self.move(direction)

class Game:
    map: list = map_pattern
    ship: Ship = Ship(30, 15)
    bullets: list = []
    aliens: list = [
        Alien(3, 5, 0),
        Alien(8, 8, 1),
        Alien(3, 11, 2),
        Alien(8, 14, 3),
        Alien(3, 17, 4),
        Alien(8, 20, 5),
        Alien(3, 23, 6),
        Alien(8, 26, 7),
    ]
    step: int = 256
    seed: int
    mask: int
    pmark: tuple = (30, 15)
    pstep: int = 0

    def __init__(self):
        self.seed = 1 # the seed you got
        self.mask = 1 # the mask you got

    def shoot(self):
        self.ship.bullet_num -= 1
        self.bullets.append(Bullet(self.ship.x, self.ship.y))

    def print_map(self):
        self.pstep += 1
        current_map = [row[:] for row in self.map[:]]
        current_map[self.ship.x][self.ship.y] = 'O'
        #print("Your position: (%d, %d)" % (self.ship.x, self.ship.y))
        for alien in self.aliens:
            current_map[alien.x][alien.y] = '*'
            if abs(self.pmark[0] - alien.x) + abs(self.pmark[1] - alien.y) <= self.pstep:
                print("Alien%d position: (%d, %d)" % (alien.order, alien.x, alien.y))
                print("Alien%d, move %d and shoot" % (alien.order, alien.y - self.pmark[1]))
                self.pstep -= abs(self.pmark[1] - alien.y) + 1
                self.pmark = (self.ship.x, alien.y)
                self.aliens.remove(alien)
        for bullet in self.bullets:
            current_map[bullet.x][bullet.y] = '^'
        # print('\n'.join([''.join(i) for i in current_map]))
        if self.step == 254:
            self.pstep = 0
            self.pmark = (self.ship.x, self.ship.y)
        

    def update(self):
        self.print_map()

        action = ''
        if action == "A":
            self.ship.move((0, -1))
            for alien in self.aliens:
                if (self.ship.x == alien.x and self.ship.y == alien.y):
                    print("You lost.")
                    exit()
        elif action == "D":
            self.ship.move((0, 1))
            for alien in self.aliens:
                if (self.ship.x == alien.x and self.ship.y == alien.y):
                    print("You lost.")
                    exit()
        elif action == "S" and self.ship.bullet_num:
            self.shoot()

        for alien in self.aliens:
            alien.random_walk(self.seed)
            if (self.ship.x == alien.x and self.ship.y == alien.y):
                print("You lost.")
                exit()
            for bullet in self.bullets:
                if (alien.x == bullet.x and alien.y == bullet.y):
                    self.aliens.remove(alien)
                    self.bullets.remove(bullet)
        self.seed *= self.mask
        self.seed %= 36583

        for bullet in self.bullets:
            if bullet.x == 1:
                print("You lost.")
                exit()
            bullet.move((-1, 0))
            for alien in self.aliens:
                if (alien.x == bullet.x and alien.y == bullet.y):
                    self.aliens.remove(alien)
                    self.bullets.remove(bullet)
                    break

        if not len(self.aliens):
            print(flag)
            exit()

        self.step -= 1

game = Game()

while game.step:
    game.update()

print("Your steps ran out...")