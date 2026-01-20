import pygame
class Transition:

    def __init__(self, x, y, tx, ty, color):
        self.x = x
        self.y = y
        self.tx = tx
        self.ty = ty 
        self.color = color
        self.size = 10
        self.speed = 0.1 
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (int(self.x), int(self.y), self.size, self.size))

    def math(self):
        self.x += (self.tx-self.x)* self.speed 
        self.y += (self.ty - self.y) * self.speed 
    
    def finished(self):
        return abs(self.tx - self.x) < 0.5 and abs(self.ty - self.y) <0.5

    def target_next(self,tx,ty):
        self.tx = tx
        self.ty = ty