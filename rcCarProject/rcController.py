from rcCar import rcCar
import time

car = rcCar()

car.forward(0.1)
time.sleep(1)

car.stop()
time.sleep(1)

car.backward(0.1)
time.sleep(1)

car.stop()
time.sleep(1)

car.rotateLeft(0.1)
time.sleep(1)

car.stop()
time.sleep(1)

car.rotateRight(0.1)
time.sleep(1)

car.stop()
time.sleep(1)