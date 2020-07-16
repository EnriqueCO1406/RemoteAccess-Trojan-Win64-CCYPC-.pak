from connection import ServerConnection
from handleConnection import handleConnection

if __name__ == "__main__":
    my_socket = ServerConnection() #Crea el socket

    my_socket.CreateConnection("", 8080) #Conexion, con IP local y puerto que va a escuchar
    
    print ("[+] Waiting for incoming connections on port: ", my_socket.server_port) 

    my_socket.Listen() #Se mantendra escuchando
    
    my_conn = my_socket.AcceptConnection() #Acepta la conexion, si una llega
    

    handleConnection(my_socket)

   # my_socket.send_data("Hi this is server")
   # print (my_socket.receive_data())
    #my_conn.close()

    my_socket.close()

    
