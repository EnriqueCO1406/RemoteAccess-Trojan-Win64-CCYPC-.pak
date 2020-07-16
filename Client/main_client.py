from connection import ClientConnection
from handleConnection import handleConnection

if __name__ == "__main__":
    my_socket = ClientConnection() #Crea el socket

    my_socket.Connect("10.10.10.2",8080) #Se conecta al host

   # print(my_socket.receive_data())
    #my_socket.send_data("Hi this is client")

    handleConnection(my_socket)

    my_socket.close()