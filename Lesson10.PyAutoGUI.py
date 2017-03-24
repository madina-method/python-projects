import pyautogui as p
import time
import webbrowser as w


#for windows - PIL -[image]- pyautogui
#for mac Xcode - pip3 install py..

"""

MOUSE

p.moveTo(1040, 22, 0.5)
p.click()
p.moveTo(300, 300, 0.5)

d = 200
while d > 0:
    p.dragRel(d, 0, 0.5)
    p.dragRel(0, d, 0.5)
    d-=20
    p.dragRel(-d, 0, 0.5)
    p.dragRel(0, -d, 0.5)
    d-=20

"""
"""

#KEYBOARD

time.sleep(2)
p.press("a") # 1 symbol
p.typewrite("Hello, world!", 0.3)


p.keyDown("command")
p.keyDown("a")
p.keyUp("a")
p.keyUp("command")

p.hotkey("command", "x")

"""

q = input("What do u want to search?\n")
w.open("http://google.com")
time.sleep(7)
p.typewrite(q, 0.2)
p.press("enter")

p.moveTo(224, 262, 1)
p.click()
time.sleep(2)
p.screenshot("123.jpg")
p.scroll(-10) 



