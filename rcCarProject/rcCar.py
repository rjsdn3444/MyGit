from rcMotor import rcMotor

class rcCar:
    def __init__(self, forwardL=21, backwardL=20, forwardR=12, backwardR=16, minSpeed=0.18, maxSpeed=1.0):
        self.__motorL = rcMotor(forwardL, backwardL, minSpeed, maxSpeed)
        self.__motorR = rcMotor(forwardR, backwardR, minSpeed, maxSpeed)

    def forward(self, speed=0):
        self.__motorL.forwardMotor(speed)
        self.__motorR.forwardMotor(speed)
    
    def backward(self, speed=0):
        self.__motorL.backwardMotor(speed)
        self.__motorR.backwardMotor(speed)

    def rotateLeft(self, speed=0):
        self.__motorL.backwardMotor(speed)
        self.__motorR.forwardMotor(speed)

    def rotateRight(self, speed=0):
        self.__motorL.forwardMotor(speed)
        self.__motorR.backwardMotor(speed)

    def stop(self):
        self.__motorL.stopMotor()
        self.__motorR.stopMotor()