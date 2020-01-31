import pygame
from network import Network
from snake import Snake
from food import Food
import time

pygame.init()

#draw window and elements
def redraw_window(win, snake, snake2, food):
    win.fill((255, 255, 255))
    food.draw(win)
    snake.draw(win)
    snake2.draw(win)
    pygame.display.update()


#main
def main():
    run = True
    game = True
    #network creation
    n = Network()
    #get snake from server
    snake = n.get_s()
    #ask for food
    food = n.send("food")
    #ask for window size
    size = n.send("size")
    #window creation
    win = pygame.display.set_mode((size, size))
    pygame.display.set_caption("Client")
    
    clock = pygame.time.Clock()

    while run:
        pygame.time.delay(50)
        clock.tick(10)

        #get snake 2 (other client)
        snake2 = n.send(snake)

        #quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        #body of snake moves
        snake.move_body()
        #head of snake moves
        snake.move()

        #if snake eats food
        if pygame.Rect(snake.get_rect()).contains(pygame.Rect(food.get_rect())):
            #ask to create new food
            n.send("create_food")
            snake.eat()

        #if collision
        if n.send("collisions") == True:
            time.sleep(1)
            #reset snakes
            snake = n.send("reset")

        #send snake2 to snake
        snake2 = n.send(snake)
        
        #send food
        food = n.send("food")
        #redraw window => update
        redraw_window(win, snake, snake2, food)
        time.sleep(0.01)


main()