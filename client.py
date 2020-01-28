import pygame
from network import Network


win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Client")

nb_client = 0

class Snake():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.velocity = 1

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= self.velocity

        if keys[pygame.K_s]:
            self.y += self.velocity

        if keys[pygame.K_a]:
            self.x -= self.velocity

        if keys[pygame.K_d]:
            self.x += self.velocity

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

   
def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + ", " + str(tup[1])

def redraw_window(win, snake, snake2):
    win.fill((255, 255, 255))
    snake.draw(win)
    snake2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    start_pos = read_pos(n.get_pos())
    snake = Snake(start_pos[0], start_pos[1], 100, 100, (0, 255, 0))
    snake2 = Snake(0, 0, 100, 100, (255, 0, 0))

    while run:

        snake2_pos = read_pos(n.send(make_pos((snake.x, snake.y))))
        snake2.x = snake2_pos[0]
        snake2.y = snake2_pos[1]
        snake2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        snake.move()
        redraw_window(win, snake, snake2)

main()