from rcMotor import rcMotor

class rcCar:
    def __init__(self):
        self.__motor = rcMotor()

    def forward(self, speed=0):
        self.__motor.forwardMotorL(speed)
        self.__motor.forwardMotorR(speed)
    
    def backward(self, speed=0):
        self.__motor.backwardMotorL(speed)
        self.__motor.backwardMotorR(speed)

    def rotateLeft(self, speed=0):
        self.__motor.backwardMotorL(speed)
        self.__motor.forwardMotorR(speed)

    def rotateRight(self, speed=0):
        self.__motor.forwardMotorL(speed)
        self.__motor.backwardMotorR(speed)

    def stop(self):
        self.__motor.stopMotorL()
        self.__motor.stopMotorR()