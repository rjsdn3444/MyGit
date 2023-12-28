# 제작자 : 김건우
# 제작일 : 2023-12-28
# 제작목표 : gazebo와 같은 시뮬레이션 프로그램 및 실제 차량에 적용할 수  있는 차 클래스 구현
# [업데이트 목록]
# 1. car 클래스의 생성자에 __minSpeed, __maxSpeed 내부변수 추가
# rc카 기준에서 모터가 낼 수 있는 최소 속도, 최고 속도가 있음을 알았다.
# rc카를 포함한 다른 환경에서도 적용할 수 있도록 Car 클래스의 생성자에 minSpeed, maxSpeed를 추가하고
# 속도와 관련된 코드들을 수정했다.
# 2. gear 내부변수 추가
# 1번 추가로 속도가 음수가 될 수 없으므로 전진 후진을 구별하는 gear 내부변수를 추가했다.
# 3. car 클래스의 생성자에 __maxAngle 내부변수 추가
# 1번과 같은 이유로 환경에 따라 차 바퀴가 꺽이는 최대 각도가 다르므로 
# car 클래스의 생성자에 maxAngle을 추가하고 방향과 관련된 코드들을 수정했다.

import time

# 시뮬레이션 테스트 차 제작
class Car:
    # 생성자
    def __init__(self, minSpeed=0.0, maxSpeed=1.0, maxAngle=1.0):
        # 클래스 내부 변수 모음

        # 운전자가 조작할 수 없는 변수 모음
        self.__realSpeed = 0. # 차의 현재 속도
        self.__realWheelAngle = 0. # 차의 현재 바퀴 방향
        self.__minSpeed = minSpeed # 차가 낼 수 있는 최소 속도
        self.__maxSpeed = maxSpeed # 차가 낼 수 있는 최고 속도
        self.__maxAngle = maxAngle # 바퀴가 최대로 꺽이는 각도

        # 운전자가 조작할 수 있는 변수 모음
        self.__speed = 0. # 운전자가 원하는 속도
        self.__wheelAngle = 0. # 운전자가 원하는 바퀴 방향
        self.__gear = True # 전진 후진 가능을 가진 기어 True=전진, False=후진

        # 시간 관련 변수 모음
        self.__startTime = time.time() # 클래스가 생성된 시간 기록

        # 기타 변수 모음 
        self.__speedChangeRate = 5.0 # 속도 변화에 쓰일 변수 / 목표값과 현재값의 차이를 구한 뒤 차이값을 변화율 만큼 나눈 값을 현재값에 적용
        self.__angleChangeRate = 5.0 # 방향 변화에 쓰일 변수 / 목표값과 현재값의 차이를 구한 뒤 차이값을 변화율 만큼 나눈 값을 현재값에 적용
    
    # 클래스 내부 함수 모음
        
    # 차를 조작하기 위해 사용할 함수 모음 
    def setSpeed(self, speed): # 목표로 하는 속도를 수정
        if speed > self.__maxSpeed:
            speed = self.__maxSpeed
        elif speed < self.__minSpeed:
            speed = 0
        self.__speed = speed

    def setWheelAngle(self, angle): # 목표로 하는 바퀴 방향을 수정
        if angle > self.__maxAngle:
            angle = self.__maxAngle
        if angle < -self.__maxAngle:
            angle = -self.__maxAngle
        self.__wheelAngle = angle

    def setGear(self, gear): # 기어를 수정
        self.__gear = gear

    # 차의 상태를 변화시키기 위한 함수 모음
    def setRealSpeed(self, speed): # 현재 속도를 수정
        if speed > self.__maxSpeed:
            speed = self.__maxSpeed
        elif speed < self.__minSpeed:
            speed = 0
        self.__realSpeed = speed
    
    def setRealWheelAngle(self, angle): # 현재 바퀴 방향을 수정
        if angle > self.__maxAngle:
            angle = self.__maxAngle
        if angle < -self.__maxAngle:
            angle = -self.__maxAngle
        self.__realWheelAngle = angle

    def applyGear(self): # 기어의 상태에 따라 realSpeed에 1.0이나 -1.0을 곱하기 위해 만든 함수
        if self.__gear == True:
            return 1.0
        else:
            return -1.0

    # 목표값을 차에 적용하는 함수 모음
    def applySituration(self): # 목표값과 현재값의 차이를 구한 뒤 차이값을 변화율 만큼 나눈 값을 현재값에 적용
        # 기어상태를 목표속도에 적용
        speed = self.__speed * self.applyGear()
        # 목표속도를 현재속도에 적용
        speedInterval = speed - self.__realSpeed
        if speedInterval == 0.0:
            self.__realSpeed = speed
        else:
            self.__realSpeed += speedInterval / self.__speedChangeRate
        # 목표방향을 현재방향에 적용
        angleInterval = self.__wheelAngle - self.__realWheelAngle
        if angleInterval == 0.0:
            self.__realWheelAngle = self.__wheelAngle
        else:
            self.__realWheelAngle += angleInterval / self.__angleChangeRate

    # 차의 상태를 리턴하는 함수 모음
    def printState(self): # 차의 모든 변수값 출력
        print(f"현재 시간 : {time.time() - self.__startTime : .2f}")
        print(f"목표 속도 : {self.__speed * self.applyGear() : 4.2f}", end="\t")
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

    def getGear(self): # 현재 기어 상태를 리턴
        return self.__gear