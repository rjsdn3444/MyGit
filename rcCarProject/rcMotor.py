from gpiozero import Motor

class rcMotor:
    def __init__(self, myForward, myBackward, minSpeed, maxSpeed):
        self.__motor = Motor(forward=myForward, backward=myBackward)
        self.__minSpeed = minSpeed
        self.__maxSpeed = maxSpeed
    
    def forwardMotor(self, mySpeed=0):
        if mySpeed < self.__minSpeed:
            mySpeed = self.__minSpeed
        if mySpeed > self.__maxSpeed:
            mySpeed = self.__maxSpeed
        self.__motor.forward(speed=mySpeed)

    def backwardMotor(self, mySpeed=0):
        if mySpeed < self.__minSpeed:
            mySpeed = self.__minSpeed
        if mySpeed > self.__maxSpeed:
            mySpeed = self.__maxSpeed
        self.__motor.backward(speed=mySpeed)

    def stopMotor(self):
        self.__motor.stop()