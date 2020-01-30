import socket
from _thread import *
from snake import Snake
from food import Food
import pickle


server = "10.103.121.52"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind ((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, Server started")

size = 500

snakes = [Snake(0, 0, 20, 20, (255, 0, 0)), Snake(480, 480, 20, 20, (0, 0, 255))]

food = Food(0, 0, 20, 20, (138, 245, 66))
food.create_food()


def threaded_client(conn, snake):
    conn.send(pickle.dumps(snakes[snake]))

    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096))

            if isinstance(data, Snake):
                snakes[snake] = data

            if not data:
                print("Disconnected")
                break
            else:
                if snake == 1:
                    reply = snakes[0]
                else:
                    reply = snakes[1]

            if data == "food":
                reply = food
            if data == "create_food":
                food.create_food()
            if data == "size":
                reply = size

                print("Recieved: ", data)
                print("Sending: ", reply)

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