import socket
import threading

# Dirección IP del servidor y puerto
HOST = ''
PORT = 5000


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creamos el socket
server.bind((HOST, PORT))
server.listen(1)

print(f"Servidor escuchando en el puerto {PORT}...")

conn, addr = server.accept()
print(f"Conectado con {addr}")


def recibir():
    while True:
        try:
            mensaje = conn.recv(1024).decode('utf-8')
            if not mensaje:
                break
            print(f"\nCliente: {mensaje}")
        except:
            print("Error en la conexión.")
            conn.close()
            break
def enviar():
    while True:
        mensaje = input("")
        conn.send(mensaje.encode('utf-8'))
# Iniciar hilos
threading.Thread(target=recibir).start()
threading.Thread(target=enviar).start()
