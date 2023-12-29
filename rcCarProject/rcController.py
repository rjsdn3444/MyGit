from rcCar import rcCar
import time
from tkinter import *

SPEED = 0.3

def Forward():
    global car
    car.forward(SPEED)
    pass

def Backward():
    global car
    car.backward(SPEED)
    pass

def RotateLeft():
    global car
    car.rotateLeft(SPEED)
    pass

def RotateRight():
    global car
    car.rotateRight(SPEED)
    pass

def Stop():
    global car
    car.stop()

def Exit():
    global window
    window.destroy()

car = rcCar()

window = Tk()
window.geometry("400x400+100+100")

blankLabel1 = Label(window, text=" ", width=10, height=5)
blankLabel1.grid(row=0, column=0)
forwardButton = Button(window, text="UP", width=10, height=5, bg="gray70", command=Forward)
forwardButton.grid(row=0, column=1)
blankLabel2 = Label(window, text=" ", width=10, height=5)
blankLabel2.grid(row=0, column=2)
rotateLeftButton = Button(window, text="LEFT", width=10, height=5, bg="gray70", command=RotateLeft)
rotateLeftButton.grid(row=1, column=0)
stopButton = Button(window, text="STOP", width=10, height=5, bg="gray70", command=Stop)
stopButton.grid(row=1, column=1)
rotateRightButton = Button(window, text="RIGHT", width=10, height=5, bg="gray70", command=RotateRight)
rotateRightButton.grid(row=1, column=2)
blankLabel4 = Label(window, text=" ", width=10, height=5)
blankLabel4.grid(row=2, column=0)
backwardButton = Button(window, text="DOWN", width=10, height=5, bg="gray70", command=Backward)
backwardButton.grid(row=2, column=1)
exitButton = Button(window, text="EXIT", width=10, height=5, bg="gray70", command=Exit)
exitButton.grid(row=2, column=2)

while(True):
    try:
        window.focus()
    except:
        break
    window.update()
    time.sleep(0.1)