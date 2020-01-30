import pygame

class Snake():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.direction = "stop"
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = 20
        self.body = []

    def get_rect(self):
        return self.rect

    def draw(self, window_game):
        body_color = (245, 66, 245)
        pygame.draw.rect(window_game, self.color, self.rect)
        if len(self.body) > 0:
            for part in self.body:
                pygame.draw.rect(window_game, body_color, part)

    def set_direction(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
           self.direction = "right"
        if keys[pygame.K_d]:
           self.direction = "left"
        if keys[pygame.K_w]:
           self.direction = "up"
        if keys[pygame.K_s]:
           self.direction = "down"

    def move(self):
        self.set_direction()
        if self.direction == "right":
           self.x -= self.velocity
        if self.direction == "left":
           self.x += self.velocity
        if self.direction == "up":
            self.y -= self.velocity
        if self.direction == "down":
            self.y += self.velocity
        self.update()

    def move_body(self):
        for index in range(len(self.body)-1, 0, -1):
            x = self.body[index-1].x
            y = self.body[index-1].y
            self.body[index].x = x
            self.body[index].y = y

        if len(self.body) > 0:
            x = self.x
            y = self.y
            self.body[0].x = x
            self.body[0].y = y
    

    
    def update(self):
        self.rect = (self.x, self.y,self.width, self.height)

    def eat(self):
        rect = pygame.Rect(0, 0, self.width, self.height)
        self.body.append(rect)