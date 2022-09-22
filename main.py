import pyautogui
from time import sleep
msg=input("Enter your message:")
numbers=int(input("enter numbers"))
for i in range(numbers+1):
    pyautogui.typewrite(msg)
    sleep(3)
    pyautogui.press("enter")
    sleep(3)

    
