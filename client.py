import pygame
from network import Network
from snake import Snake
from food import Food
import time

pygame.init()

def redraw_window(win, snake, snake2, food):
    win.fill((255, 255, 255))
    food.draw(win)
    snake.draw(win)
    snake2.draw(win)
    pygame.display.update()


def main():
    run = True
    game = True
    n = Network()
    snake = n.get_s()
    food = n.send("food")
    size = n.send("size")
    win = pygame.display.set_mode((size, size))
    pygame.display.set_caption("Client")
    
    clock = pygame.time.Clock()

    while run:
        pygame.time.delay(50)
        clock.tick(10)

        snake2 = n.send(snake)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        snake.move_body()
        snake.move()

        if pygame.Rect(snake.get_rect()).contains(pygame.Rect(food.get_rect())):
            n.send("create_food")
            snake.eat()

        full_snake2 = [pygame.Rect(snake2.rect)]
        for body in snake2.body:
            full_snake2.append(pygame.Rect(body))

        full_snake = []
        for body in snake.body:
            full_snake.append(pygame.Rect(body))
        

        if pygame.Rect(snake.get_rect()).collidelist(full_snake2) != -1:
            time.sleep(1)
        if pygame.Rect(snake.get_rect()).collidelist(full_snake) != -1:
            print("did you really tried to eat yourself ?!")
        
        food = n.send("food")
        redraw_window(win, snake, snake2, food)
        time.sleep(0.01)


main()