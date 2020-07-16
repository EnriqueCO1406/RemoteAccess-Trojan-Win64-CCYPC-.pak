import json

DELIMETER = "<END_OF_RESULTS>"
CHUNK_SIZE = 4 * 1024

def receive_file_folders(my_socket):
    print("[+] Receiving Files / Folders")

    full_list = b''
    while True:
        chunk = my_socket.client_conn.recv(CHUNK_SIZE)

        if chunk.endswith(DELIMETER.encode()):
            chunk = chunk[:-len(DELIMETER)]
            full_list += chunk
            break
        full_list += chunk
    
    files_dict = json.loads(full_list)

    for index in files_dict:
        print("\t\t", index, "\t", files_dict[index])

    file_index = input("[+] Select the file/folder")
    file2download = files_dict[file_index]

    print("[+] User selected: ", file2download)
    my_socket.send_data(file2download)

    print("[+] Receiving zipped file")

    zipped_file = file2download + ".zip"
    print("[+] Received name:", zipped_file)

    my_socket.receive_zipped(zipped_file)