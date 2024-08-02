import KeyboardModule as kp
from djitellopy import tello
from time import sleep

kp.init()

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

def getInput():
    sides, boards, alt, yaw = 0, 0, 0, 0    #This variables set initial parameters for the four ways of movimentation
    speed = 50

    if kp.getKey("LEFT"): sides = -speed
    elif kp.getKey("RIGHT"): sides = speed

    if kp.getKey("UP"): boards = speed
    elif kp.getKey("DOWN"): boards = -speed

    if kp.getKey("w"): alt = speed
    elif kp.getKey("s"): alt = -speed

    if kp.getKey("d"): yaw = speed
    elif kp.getKey("a"): yaw = -speed

    #if kp.getKey("q"): drone.takeoff()
    if kp.getKey("e"): drone.land()

    return [sides, boards, alt, yaw]

drone.takeoff()

while True:
    values = getInput()
    drone.send_rc_control(values[0], values[1], values[2], values[3])
    sleep(0.05)