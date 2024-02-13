#coding:utf-8
# C:\Users\ma0is\Desktop\programmation\python\stupid_shit\socket

import socket
import threading

class ThreadForClient(threading.Thread):
    """ Class pour gerer le threading """
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        data = self.conn.recv(1024)
        data = data.decode('utf8')
        print(data)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------


host, port = ('', 5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reference l'adresse et le port
socket.bind((host, port))

print('Le serveur démarre')

while True:
    # ecoute le clien, gere le nombre d'erreur de connection avant de refuser toutes les connections
    socket.listen()
    conn, address = socket.accept()
    print('Un clien vient de se connecter..')

    my_thread = ThreadForClient(conn)
    my_thread.start()



# fermer la connection et le socket
conn.close()
socket.close()