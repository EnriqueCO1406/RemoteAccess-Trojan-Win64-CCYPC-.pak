from glob import glob
import os
#from main_server import my_socket #REVISAR

#LEER UN ARCHIVO DESDE EL HOST
#LEERLO EN LA FORMA DE BYTES
#DELIMETER PARA SABER DONDE ACABA EL ARCHIVO
#TRANSFERIR UN ARCHIVO SOBRE LA RED
#RECIBIR EL ARCHIVO DEL LADO DEL CLIENTE
#REMOVER DELIMETER PARA RECIBIR LA DATA ORIGINAL
#ESCRIBIR EL ARCHIVO EN EL DISCO


def upload_files(my_socket):
    print("[+] Upload files")

    files = glob("*")

    for index, filename in enumerate(files):
        
        new_filename = os.path.basename(filename) #Obtener el nombre sin la direccion completa
        print("\t\t", index, "\t", new_filename)
        
    while True:
        try:
            file_index = int(input("[+] Select file: "))
            if len(files) >= file_index >= 0:
                filename = files[file_index]
                break
        except:
            print("[-] invalid file selected")

    print("[+] Selected files = ", filename)

    my_socket.send_data(filename)

    my_socket.send_file(filename)



    

