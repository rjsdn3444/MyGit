# 제작자 : 김건우
# 제작일 : 2023-12-28
# [업데이트 목록]
# SimulationTestCar_v_0_2에 맞게 버튼 이벤트 함수, gui버튼 모두 수정
# 전, 후, 좌, 우 4개의 버튼을 구현했던 전 버전과 달리 현실적인 차와 조작법이 비슷해지도록 수정했다.
# 좌, 우 버튼은 핸들을 좌 우로 꺽는 느낌으로 위에 배치
# 전, 후 버튼을 삭제하고 엑셀, 브레이크 버튼을 추가
# 전진, 후진 기능이 있는 기어 버튼 추가

from STcar.SimulationTestCar_v_0_2 import Car as stCar
import time
from tkinter import *
import os

# 버튼 이벤트 함수 모음
def handleLeft():
    global car1
    car1.setWheelAngle(car1.getWheelAngle() - 0.1)

def handleRight():
    global car1
    car1.setWheelAngle(car1.getWheelAngle() + 0.1)

def pushAccel():
    global car1
    car1.setSpeed(car1.getSpeed() + 0.1)

def pushBrake():
    global car1
    car1.setSpeed(car1.getSpeed() - 0.1)

def changeGear():
    global car1
    car1.setGear(not car1.getGear())

# 차 생성
car1 = stCar()

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
