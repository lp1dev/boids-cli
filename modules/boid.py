class Boid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1
        self.char = "A"

    def towards(self, x, y):
        if x > self.x:
            self.x += self.speed
        elif x < self.y:
            self.x -= self.speed
        if y > self.y:
            self.y += self.speed
        elif y < self.y:
            self.y -= self.speed
