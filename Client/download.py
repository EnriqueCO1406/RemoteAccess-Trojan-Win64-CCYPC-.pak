
def download_files(my_socket):
    print("[+] Downloading files")

    filename = my_socket.receive_data()

    my_socket.receive_file(filename)
