import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.103.121.52"
        #self.server = "192.168.100.11"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.s = self.connect()

    def get_s(self):
        return self.s

    #connect client to server
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(4096))
        except:
            pass

    #send data to server
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)

