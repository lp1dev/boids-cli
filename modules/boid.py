import numpy as np

class Boid:
    def __init__(self, x, y, speed=1):
        self.x = x
        self.y = y
        self.vector = np.array([x, y])
        self.speed = speed
        self.char = "A"
        
    def towards(self, x, y):
        if x > self.x:
            self.x += self.speed
            self.char = 'A'
        elif x < self.x:
            self.x -= self.speed
            self.char = 'V'
        if y > self.y:
            self.y += self.speed
            self.char = '>'
        elif y < self.y:
            self.y -= self.speed
            self.char = '<'
