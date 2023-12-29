from gpiozero import Motor

class rcMotor:
    def __init__(self, forwardL=21, backwardL=20, forwardR=12, backwardR=16, minSpeed=0.18, maxSpeed=1.0):
        self.__motorL = Motor(forward=forwardL, backward=backwardL)
        self.__motorR = Motor(forward=forwardR, backward=backwardR)
        self.__minSpeed = minSpeed
        self.__maxSpeed = maxSpeed
    
    def forwardMotorL(self, mySpeed=0):
        if mySpeed < self.__minSpeed:
            mySpeed = self.__minSpeed
        if mySpeed > self.__maxSpeed:
            mySpeed = self.__maxSpeed
        self.__motorL.forward(speed=mySpeed)

    def backwardMotorL(self, mySpeed=0):
        if mySpeed < self.__minSpeed:
            mySpeed = self.__minSpeed
        if mySpeed > self.__maxSpeed:
            mySpeed = self.__maxSpeed
        self.__motorL.backward(speed=mySpeed)

    def stopMotorL(self):
        self.__motorL.stop()

    def forwardMotorR(self, mySpeed=0):
        if mySpeed < self.__minSpeed:
            mySpeed = self.__minSpeed
        if mySpeed > self.__maxSpeed:
            mySpeed = self.__maxSpeed
        self.__motorR.forward(speed=mySpeed)

    def backwardMotorR(self, mySpeed=0):
        if mySpeed < self.__minSpeed:
            mySpeed = self.__minSpeed
        if mySpeed > self.__maxSpeed:
            mySpeed = self.__maxSpeed
        self.__motorR.backward(speed=mySpeed)

    def stopMotorR(self):
        self.__motorR.stop()