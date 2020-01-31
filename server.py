import socket
from _thread import *
from snake import Snake
from food import Food
import pickle
import pygame


server = "10.103.121.52"
#server = "192.168.100.11"
port = 5555

#create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind socket
try:
    s.bind ((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, Server started")

#window size (square)
size = 500

#creation of snakes
snakes = [Snake(0, 0, 20, 20, (255, 0, 0)), Snake(480, 480, 20, 20, (0, 0, 255))]

#creation of food
food = Food(0, 0, 20, 20, (138, 245, 66))
#ask for method of creating random position for food (class Food)
food.create_food()

#thread to get and send data
def threaded_client(conn, snake):
    #send snakes
    conn.send(pickle.dumps(snakes[snake]))

    reply = ""
    while True:
        try:
            #get data
            data = pickle.loads(conn.recv(4096))

            #data is instance of snake
            if isinstance(data, Snake):
                snakes[snake] = data

                #no data => disconnect
            if not data:
                print("Disconnected")
                break
            else:
                if isinstance(data, Snake):
                    if snake == 1:
                        reply = snakes[0]
                    else:
                        reply = snakes[1]

                if data == "food":
                    reply = food
                if data == "create_food":
                    #ask for method of creating random position for food (class Food) 
                    food.create_food()
                if data == "size":
                    reply = size
                if data == "collisions":
                    #collisions
                    #collision head of snake with body
                    if snakes[0].body_collisions() != -1 or snakes[1].body_collisions() != -1:
                        reply = True
                    #collision snake with snake
                    elif pygame.Rect(snakes[0].rect).collidelist(snakes[1].get_snake_body()) != -1 or pygame.Rect(snakes[1].rect).collidelist(snakes[0].get_snake_body()) != -1:
                        reply = True
                    else:
                        reply = False
                #reset snakes
                if data == "reset":
                    if snake == 1:
                        reply = Snake(480, 480, 20, 20, (0, 0, 255))
                    if snake == 0:
                        reply = Snake(0, 0, 20, 20, (255, 0, 0))


            #print("Recieved: ", data)
            #print("Sending: ", reply)

            #send reply
            conn.sendall(pickle.dumps(reply))

        except:
            break

    print("Lost connection")
    conn.close()

current_player = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1