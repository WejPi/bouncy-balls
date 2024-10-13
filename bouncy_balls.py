import pygame
import pygame.display
import pygame.draw
import pygame.sprite
from random import randint

class Ball(pygame.sprite.Sprite):
    def __init__(self,color,x,y,radius):
        super().__init__()
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.DIRECTION_X = 1
        self.DIRECTION_Y = 1

    def draw(self,surface):
        pygame.draw.circle(surface,self.color,(self.x,self.y),self.radius,self.radius)


class Main():
    def __init__(self,width,height):
        self.WIDTH = width
        self.HEIGHT = height
        self.SPEED_X = 0.3
        self.SPEED_Y = 0.3
    def components(self):
        self.window = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
    def Loop(self):
        self.run = True
        self.ball1 = Ball("green",self.WIDTH/2,self.HEIGHT/2,50)

        self.ball1.x = randint(50,self.WIDTH-50)
        self.ball1.y = randint(50,self.HEIGHT-50)
        self.ball1.DIRECTION_X = randint(-1,1)
        self.ball1.DIRECTION_Y = randint(-1,1)
        if self.ball1.DIRECTION_X == 0:
            self.ball1.DIRECTION_X = 1
        if self.ball1.DIRECTION_Y == 0:
            self.ball1.DIRECTION_Y = 1

        while self.run == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.window.fill("black")
            
            
            self.ball1.draw(self.window)
            self.ball1.x += self.SPEED_X*self.ball1.DIRECTION_X
            self.ball1.y += self.SPEED_Y*self.ball1.DIRECTION_Y

            if self.ball1.x<50 or self.ball1.x>750:
                self.ball1.DIRECTION_X*=-1
            if self.ball1.y<50 or self.ball1.y>550:
                self.ball1.DIRECTION_Y*=-1


            pygame.display.update()


window = Main(800,600)
window.components()
window.Loop()