import pygame
import pygame.display
import pygame.draw
import pygame.math
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
        self.RADIUS = 50
        self.NUMBER_OF_BALLS = 3
    def components(self):
        self.window = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
    def Loop(self):
        self.run = True
        self.balls = []
        for i in range(self.NUMBER_OF_BALLS):
            self.balls.append(Ball("green",self.WIDTH/2+randint(-10,10),self.HEIGHT/2+randint(-10,10),self.RADIUS))


        for ball in self.balls:
            ball.x = randint(self.RADIUS,self.WIDTH-self.RADIUS)
            ball.y = randint(self.RADIUS,self.HEIGHT-self.RADIUS)
            ball.DIRECTION_X = randint(-1,1)
            ball.DIRECTION_Y = randint(-1,1)
            if ball.DIRECTION_X == 0:
                ball.DIRECTION_X = 1
            if ball.DIRECTION_Y == 0:
                ball.DIRECTION_Y = 1
        

        while self.run == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.window.fill("black")
            
            
            for ball in self.balls:
                ball.draw(self.window)
                ball.x += self.SPEED_X*ball.DIRECTION_X
                ball.y += self.SPEED_Y*ball.DIRECTION_Y

                if ball.x<self.RADIUS or ball.x>self.WIDTH-self.RADIUS:
                    ball.DIRECTION_X*=-1
                if ball.y<self.RADIUS or ball.y>self.HEIGHT-self.RADIUS:
                    ball.DIRECTION_Y*=-1
                
            

            for i in range(len(self.balls)):
                for j in range(i+1,len(self.balls)):
                    dx = self.balls[i].x - self.balls[j].x
                    dy = self.balls[i].y - self.balls[j].y
                    distance = (dx**2+dy**2)**0.5
                    if distance<2*self.RADIUS:
                        self.balls[i].x, self.balls[j].x = self.balls[j].x, self.balls[i].x
                        self.balls[i].y, self.balls[j].y = self.balls[j].y, self.balls[i].y

            pygame.display.update()


window = Main(800,600)
window.components()
window.Loop()