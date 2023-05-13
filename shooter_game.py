#Создай собственный Шутер!

from pygame import *
from random import randint

counter = 0

Width = 1024
Height = 768


sc = display.set_mode([Width, Height])
display.set_caption("War thander")
galaxy = transform.scale(image.load("resp.jpg"), (Width, Height))
mixer.init()
mixer.music.load("tzub.mp3")
mixer.music.play(-1)
clock = time.Clock()
FPS = 144
x, y = 0, 0
dirs = {"a": True, "d": True}

# rocket1 = transform.scale(
#     image.load("rocket.png"),
#     (100, 100)    
# )

ufo1 = transform.scale(
    image.load("ufo.png"),
    (100, 100)
)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, w,h):
        super().__init__()
        self.player_image = transform.scale(image.load(player_image), (w, h))
        self.player_speed = player_speed
        self.rect = self.player_image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.shotFlag = False
    def reset(self):
        sc.blit(self.player_image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        # if key[K_s] and self.rect.y <= 90:
        #     self.rect.y += self.player_speed
        # if key[K_w] and self.rect.y <= 90:
        #     self.rect.y += self.player_speed
        if keys[K_a] and self.rect.x >= 90:
            self.rect.x -= self.player_speed
        if keys[K_d] and self.rect.x <= 934:
            self.rect.x += self.player_speed






class Enemy(GameSprite):
    def update(self):
        self.rect.y += 1
        if self.rect.y >= Height or sprite.collide_rect(ufo1, bullet):
            self.rect.y = 0
            self.rect.x = randint(0, Width)
            


# monsters = sprite.Group()
# monsters.add(ufo1)


class Player(GameSprite):
    
    def update(self):
        keys = key.get_pressed()
        # if key[K_s] and self.rect.y <= 90:
        #     self.rect.y += self.player_speed
        # if key[K_w] and self.rect.y <= 90:
        #     self.rect.y += self.player_speed
        if keys[K_a] and self.rect.x >= 90:
            self.rect.x -= self.player_speed
        if keys[K_d] and self.rect.x <= 934:
            self.rect.x += self.player_speed
    def scoreCount(self):
        if sprite.collide_rect(bullet, ufo1):
            global counter
            counter += 1




class Bullet(GameSprite):
    def update(self):
        self.rect.x = rocket1.rect.x
    def shot(self):
        keys = key.get_pressed()
        if keys[K_c] and self.shotFlag == False:
            self.shotFlag = True
        if self.shotFlag and self.rect.y >= 0:
            self.rect.y -= self.player_speed
        elif self.rect.y < 0 or sprite.collide_rect(ufo1, bullet):
            self.rect.y = rocket1.rect.y
            self.shotFlag = False


 



font.init()
font = font.SysFont(None, 70)









ufo1 = Enemy("ballas.png", 10, randint(0, Width), 0, 200, 150)
rocket1 = Player("aztek.png", 3, 470, 650, 200, 150)
bullet = Bullet('bullet.png', 7, 470, 650, 20, 20)





game = True
while game :
    sc.blit(galaxy,(0, 0))
    score = font.render(
    'СЧЁТ' +str(counter) , True, (255, 215, 0))
    sc.blit(score, (0, 0))
    rocket1.reset()
    bullet.shot()
    bullet.reset()
    rocket1.update()
    bullet.update()
    rocket1.scoreCount()
    ufo1.reset()
    ufo1.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()


