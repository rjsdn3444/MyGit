# 제작자 : 김건우
# 제작일 : 2023-12-28
# [업데이트 목록]
# SimulationTestRealCar_v_0_1을 테스트 하기 위해 테스트 GUI를 만들었다.

from STcar.SimulationTestRealCar_v_0_1 import STRcar as strCar
import time
from tkinter import *
import os

# 버튼 이벤트 함수 모음
def handleLeft():
    global car1
    car1.handleLeft()

def handleRight():
    global car1
    car1.handleRight()

def pushAccel():
    global car1
    car1.pushAccel()

def pushBrake():
    global car1
    car1.pushBrake()

def changeGear():
    global car1
    car1.changeGear()

# 차 생성
car1 = strCar()

# GUI 설정
window = Tk()
window.geometry("300x300+100+100")

# 출력화면 설정
label1 = Label(window, text=f"목표속도 : {car1.getSpeed() * car1.applyGear(): 3.3f}\t목표방향 : {car1.getWheelAngle() : 3.3f}", width=39, height=1, bg="gray100")
label1.place(x=10, y=10)
label2 = Label(window, text=f"현재속도 : {car1.getRealSpeed(): 3.3f}\t현재방향 : {car1.getRealWheelAngle() : 3.3f}", width=39, height=1, bg="gray100")
label2.place(x=10, y=30)

# 핸들 버튼
pushAccelButton = Button(window, text="<- [핸", width=10, height=5, bg="gray70", repeatdelay=10, repeatinterval=10, command=handleLeft)
pushAccelButton.place(x=10, y=60)
pushBrakeButton = Button(window, text="들] ->", width=10, height=5, bg="gray70", repeatdelay=10, repeatinterval=10, command=handleRight)
pushBrakeButton.place(x=100, y=60)

# 페달 버튼
pushAccelButton = Button(window, text="엑셀", width=10, height=5, bg="gray70", repeatdelay=10, repeatinterval=10, command=pushAccel)
pushAccelButton.place(x=100, y=160)
pushBrakeButton = Button(window, text="브레이크", width=10, height=5, bg="gray70", repeatdelay=10, repeatinterval=10, command=pushBrake)
pushBrakeButton.place(x=10, y=160)

# 기어 버튼
gearText = ["기어 D", "기어 R"]
gearButton = Button(window, text=gearText[0], width=10, height=5, bg="gray70", command=changeGear)
gearButton.place(x=190, y=160)

# GUI 실행
while(True):
    try: # 윈도우가 사라지면 에러를 받고 루프 종료
        window.focus()
    except:
        break

    car1.applySituration() # 차 상태 갱신
    
    # 위젯 내용 업데이트
    label1["text"] = f"목표속도 : {car1.getSpeed() * car1.applyGear(): 3.3f}\t목표방향 : {car1.getWheelAngle() : 3.3f}"
    label2["text"] = f"현재속도 : {car1.getRealSpeed(): 3.3f}\t현재방향 : {car1.getRealWheelAngle() : 3.3f}"
    if car1.getGear() == True:
        gearButton["text"] = gearText[0]
    else:
        gearButton["text"] = gearText[1]

    window.update() # 윈도우 업데이트
    time.sleep(0.1) # 잠시 대기