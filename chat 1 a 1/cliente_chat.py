import socket
import threading


SERVER_IP = input("Introduce la IP del servidor: ") # se pone la dirección IP del servidor
PORT = 5000

# Creamos el socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))
print("Conectado al servidor - A CHATEAR\n")
def recibir():
    while True:
        try:
            mensaje = client.recv(1024).decode('utf-8')
            if not mensaje:
                break
            print(f"\nServidor: {mensaje}")
        except:
            print("Conexión cerrada")
            client.close()
            break
def enviar():
    while True:
        mensaje = input("")
        client.send(mensaje.encode('utf-8'))
# Iniciar hilos
threading.Thread(target=recibir).start()
threading.Thread(target=enviar).start()
