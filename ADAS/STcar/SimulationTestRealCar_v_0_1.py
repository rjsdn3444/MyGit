# 제작자 : 김건우
# 제작일 : 2023-12-28
# 제작목표 : gazebo와 같은 시뮬레이션 프로그램 및 실제 차량에 적용할 수  있는 차 클래스 구현
# [설명]
# carname = STRcar() : STRcar 하나가 만들어진다.
# carname = STRcar(minSpeed=0.0, maxSpeed=1.0, maxAngle=1.0, accelRate = 0.1, brakeRate = 0.1, handleRate = 0.1, degree = 0.001)
# : 세부적인 설정을 추가하여 생성한다. 관련 내용은 아래 __init__을 확인
# handleLeft() : 핸들을 왼쪽으롤 회전한다.
# handleRight() : 핸들을 오른쪽으로 회전한다.
# pushAccel() : 엑셀을 누른다. / 엑셀을 조금 누르는 것은 구현하지 않았다.
# pushBrake() : 브레이크를 누른다. / 브레이크를 조금 누르는 것은 구현하지 않았다.
# changeGear(True or False) : 기어를 바꾼다. / True = 전진, False = 후진
# applySituration() : 조작값을 받아들여 현실적인 현재속도와 방향으로 전환한다. 한번 선언시 한번만 수행하므로 주기적으로 선언해야 한다.
# 해당 파일의 테스트 코드는 ADAS/test_real_v_0_1.py 이다.

from STcar.SimulationTestCar_v_0_2 import Car

# 더 현실적인 차 구현
class STRcar(Car):
    # 생성자 설정
    def __init__(self, minSpeed=0.0, maxSpeed=1.0, maxAngle=1.0, accelRate = 0.1, brakeRate = 0.1, handleRate = 0.1, degree = 0.001):
        super().__init__(minSpeed, maxSpeed, maxAngle)
        self.__accelRate = accelRate # 엑셀 밟을 시 가속하는 정도
        self.__brakeRate = brakeRate # 브레이크 밟을 시 감속하는 정도
        self.__handleRate = handleRate # 핸들 회전 정도
        self.__degree = degree # 차가 자체적으로 감속하는 속도

    # 핸들 구현
    def handleLeft(self): # 핸들 왼쪽으로 회전
        self.setWheelAngle(self.getWheelAngle() - self.__handleRate)

    def handleRight(self): # 핸들 오른쪽으로 회전
        self.setWheelAngle(self.getWheelAngle() + self.__handleRate)

    def pushAccel(self): # 엑셀 구현
        self.setSpeed(self.getSpeed() + self.__accelRate)
    
    def pushBrake(self): # 브레이크 구현
        self.setSpeed(self.getSpeed() - self.__brakeRate)
        self.setRealSpeed(self.getRealSpeed() - self.__brakeRate)

    def changeGear(self): # 기어 구현
        self.setGear(not self.getGear())

    def applySituration(self): # 상태 적용 함수 / 한 틱마다 연산
        self.setSpeed(self.getSpeed() - self.__degree)
        super().applySituration()