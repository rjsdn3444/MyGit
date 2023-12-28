# 제작자 : 김건우
# 제작일 : 2023-12-27
# 제작목표 : gazebo와 같은 시뮬레이션 프로그램 및 실제 차량에 적용할 수  있는 차 클래스 구현

import time

# 시뮬레이션 테스트 차 제작
class Car:
    # 생성자
    def __init__(self):
        # 클래스 내부 변수 모음

        # 운전자가 조작할 수 없는 변수 모음
        self.__realSpeed = 0. # 차의 현재 속도 km/h
        self.__realWheelAngle = 0. # 차의 현재 바퀴 방향 [left] -40.0 ~ 0.0 ~ +40.0 [right]

        # 운전자가 조작할 수 있는 변수 모음
        self.__speed = 0. # 운전자가 원하는 속도 km/h
        self.__wheelAngle = 0. # 운전자가 원하는 바퀴 방향 [left] -40.0 ~ 0.0 ~ +40.0 [right]

        # 시간 관련 변수 모음
        self.__startTime = time.time() # 클래스가 생성된 시간 기록
        self.__changeSpeedTime = time.time() # 목표 속도가 변경된 시간 기록
        self.__changeWheelAngleTime = time.time() # 목표 방향이 변경된 시간 기록

        # 기타 변수 모음 
        self.__speedChangeRate = 5.0 # 속도 변화에 쓰일 변수 / 목표값과 현재값의 차이를 구한 뒤 차이값을 변화율 만큼 나눈 값을 현재값에 적용
        self.__angleChangeRate = 5.0 # 방향 변화에 쓰일 변수 / 목표값과 현재값의 차이를 구한 뒤 차이값을 변화율 만큼 나눈 값을 현재값에 적용
    
    # 클래스 내부 함수 모음
        
    # 차를 조작하기 위해 사용할 함수 모음 
    def setSpeed(self, speed): # 목표로 하는 속도를 수정
        self.__speed = speed
        self.__changeSpeedTime = time.time()

    def setWheelAngle(self, angle): # 목표로 하는 바퀴 방향을 수정
        if angle > 40.0:
            angle = 40.0
        if angle < -40.0:
            angle = -40.0
        self.__wheelAngle = angle
        self.__changeWheelAngleTime = time.time()

    # 차의 상태를 변화시키기 위한 함수 모음
    def setRealSpeed(self, speed): # 현재 속도를 수정
        self.__realSpeed = speed
    
    def setRealWheelAngle(self, angle): #현재 바퀴 방향을 수정
        if angle > 40.0:
            angle = 40.0
        if angle < -40.0:
            angle = -40.0
        self.__realWheelAngle = angle

    # 목표값을 차에 적용하는 함수 모음
    def applySituration(self, OnOff=True): # 목표값과 현재값의 차이를 구한 뒤 차이값을 변화율 만큼 나눈 값을 현재값에 적용
        if OnOff == False:
            self.__realSpeed = self.__speed
            self.__realWheelAngle = self.__wheelAngle
        else:
            speedInterval = self.__speed - self.__realSpeed
            if speedInterval == 0.0:
                self.__realSpeed = self.__speed
            else:
                self.__realSpeed += speedInterval / self.__speedChangeRate
            angleInterval = self.__wheelAngle - self.__realWheelAngle
            if angleInterval == 0.0:
                self.__realWheelAngle = self.__wheelAngle
            else:
                self.__realWheelAngle += angleInterval / self.__angleChangeRate

    # 차의 상태를 리턴하는 함수 모음
    def printState(self): # 차의 모든 변수값 출력
        print(f"현재 시간 : {time.time() - self.__startTime : .2f}")
        print(f"목표 속도 : {self.__speed : 4.2f}", end="\t")
        print(f"현재 속도 : {self.__realSpeed : 4.2f}", end="\t")
        print(f"변화 속도 : {(self.__speed - self.__realSpeed)/self.__speedChangeRate : 4.2f}")
        print(f"목표 방향 : {self.__wheelAngle : 4.2f}", end="\t")
        print(f"현재 방향 : {self.__realWheelAngle : 4.2f}", end="\t")
        print(f"변화 방향 : {(self.__wheelAngle - self.__realWheelAngle)/self.__angleChangeRate : 4.2f}")
        print()
    def getSpeed(self): # 목표로 하는 속도를 리턴
        return self.__speed

    def getRealSpeed(self): # 현재 속도를 리턴
        return self.__realSpeed

    def getWheelAngle(self): # 목표로 하는 바퀴 방향을 리턴
        return self.__wheelAngle

    def getRealWheelAngle(self): # 현재 바퀴 방향을 리턴
        return self.__realWheelAngle
