import pyautogui , time
time.sleep(5)
f = open("file.txt" , "r")
while True:
    for lines in f:
        pyautogui.typewrite(lines)
        pyautogui.press("enter")