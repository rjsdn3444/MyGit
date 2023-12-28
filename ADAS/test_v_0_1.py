# 제작자 : 김건우
# 제작일 : 2023-12-27

from STcar.SimulationTestCar_v_0_1 import Car as stCar
import time
from tkinter import *
import os

# 버튼 이벤트 함수 모음
def speedUp():
    global car1
    car1.setSpeed(car1.getSpeed() + 10)

def speedDown():
    global car1
    car1.setSpeed(car1.getSpeed() - 10)

def angleLeft():
    global car1
    car1.setWheelAngle(car1.getWheelAngle() - 4)

def angleRight():
    global car1
    car1.setWheelAngle(car1.getWheelAngle() + 4)

# 차 생성
car1 = stCar()

# GUI 설정
window = Tk()
window.geometry("300x300+100+100")

speedLabel = Label(window, text=f"목표 속도 : {car1.getSpeed():4.2f}", width=30, height=1)
speedLabel.place(x=0, y=180)
realSpeedLabel = Label(window, text=f"현재 속도 : {car1.getRealSpeed():4.2f}", width=30, height=1)
realSpeedLabel.place(x=0, y=200)
angleLabel = Label(window, text=f"목표 방향 : {car1.getWheelAngle():4.2f}", width=30, height=1)
angleLabel.place(x=0, y=220)
realAngleLabel = Label(window, text=f"현재 방향 : {car1.getRealWheelAngle():4.2f}", width=30, height=1)
realAngleLabel.place(x=0, y=240)
upButton = Button(window, text="speedUP", width=10, height=5, bg="gray70", command=speedUp)
upButton.grid(row=1, column=1)
downButton = Button(window, text="speedDOWN", width=10, height=5, bg="gray70", command=speedDown)
downButton.grid(row=2, column=1)
leftButton = Button(window, text="angleLEFT", width=10, height=5, bg="gray70", command=angleLeft)
leftButton.grid(row=2, column=0)
rightButton = Button(window, text="angleRIGHT", width=10, height=5, bg="gray70", command=angleRight)
rightButton.grid(row=2, column=2)

# GUI 실행
while(True):
    car1.applySituration()
    speedLabel["text"] = f"목표 속도 : {car1.getSpeed():4.2f}"
    realSpeedLabel["text"] = f"현재 속도 : {car1.getRealSpeed():4.2f}"
    angleLabel["text"] = f"목표 방향 : {car1.getWheelAngle():4.2f}"
    realAngleLabel["text"] = f"현재 방향 : {car1.getRealWheelAngle():4.2f}"
    # os.system("cls")
    # car1.printState()
    window.update()
    time.sleep(0.1)
