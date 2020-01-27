from random import *

#board
nbColumns = 15
nbRows = 20

#moving elements
snake = ['*']
food = '+'

#print gameboard, food and snake
def createGameBoard():
	createFood()
	for i in range(0, nbColumns+1):
		for j in range(0, nbRows+1):
			if i == randCol:
				if j == randRow:
					print(food)
			else:
				print('.')

				
#create random location for food
def createFood():
	randCol = randint(1,15)
	randRow = randint(1,20)
	return randRow, randCol


#growing snake when eat
def growSnake():
	snake.append('*')

