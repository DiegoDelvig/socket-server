#coding:utf-8
import socket

# mettre l'adress IP local et le meme port que le serveur
host, port = ('127.0.0.1', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # se connecter au serveur
    socket.connect((host, port))
    print('connecter au serveur')

    data = "Bonjour a tous"
    data = data.encode("utf8")
    socket.sendall(data)

except ConnectionRefusedError:
    print('Connexion au seveur echouer')
except Exception as e:
    print(e)

finally:
    socket.close()