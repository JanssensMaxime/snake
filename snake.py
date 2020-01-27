import pygame


from random import *
from pygame.locals import *


#snake : move, eat, die, bit his body
#food : appear, be eaten
#board : print, evovlve with game

#board
nbColumns = 15
nbRows = 20

#snake position
snakeCol = 7
snakeRow = 1

#food position
foodCol = 0
foodRow = 0

#moving elements
snakeHead = ['*']
food = '+'

#game itself
continuer = 1
while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
		print('hello coucou')
	



#TODO
#print gameboard, food and snake
def createGameBoard():
	createFood()
	for i in range(0, nbColumns+1):
		for j in range(0, nbRows+1):
			if i == foodCol:
				if j == foodRow:
					print(food)
			else:
				print('.')

				
#create random location for food
def createFood(foodRow, foodCol):
	foodCol = randint(1,15)
	foodRow = randint(1,20)


#growing snake when eat
def growSnake():
	snakeHead.append('*')


#snake eats food
def eat():
	if snakeCol == foodCol:
		if snakeRow == foodRow:
			growSnake()


#moving snake
def moveSnake(snakeCol, snakeRow):
	if event.type == K_z:
		snakeRow = snakeRow+1
	elif event.type == K_s:
		snakeRow = snakeRow-1
	elif event.type == K_q:
		snakeCol = snakeCol-1
	elif event.type == K_d:
		snakeCol = snakeCol+1


