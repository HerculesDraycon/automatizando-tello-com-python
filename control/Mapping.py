import time                        #Library for manipulation of events based in time
import numpy                       #Library for matrix operations in Python
import math                        #Library for mathematic operations in Python
import cv2                         #Library for capture show on the computer
import KeyboardModule as kp        #Importing the keyboard module
from djitellopy import tello       #Library for interaction with Tello

##############PARAMETERS##############
fwdSpeed = 117/10    #Drone forward speed in cm/s
angSpeed = 360/10    #Drone rotation speed in degrees/s
interval = 0.25      #Interval in seconds of value checking

trjInterval = fwdSpeed * interval    #Trajetory calculated in the interval
angInterval = angSpeed * interval    #Rotation calculated in the interval
#######################################

x, y = 250, 250                      #Variables that place the circle in middle-screen
points = []                          #Vector of points to be positioned on the screen     
ang = 0
heading = 0

kp.init()          #Initialize the keyboard module to be able to detect keys being pressed

drone = tello.Tello()            #Instance of Tello
drone.connect()                  #Stablish connection with the Tello

print("The drone battery level is: ")
print(drone.get_battery())       #Get the drone battery level

def getInput():
    sides, boards, alt, yaw = 0, 0, 0, 0    #This variables set initial parameters for the four ways of movimentation
    speed = 15
    aSpeed = 50
    trj = 0
    global heading, ang, x, y

    if kp.getKey("LEFT"):
        sides = -speed
        trj = trjInterval
        ang = -180

    elif kp.getKey("RIGHT"):
        sides = speed
        trj = -trjInterval
        ang = 180

    if kp.getKey("UP"):
        boards = speed
        trj = trjInterval
        ang = 270

    elif kp.getKey("DOWN"):
        boards = -speed
        trj = -trjInterval
        ang = -90

    if kp.getKey("w"):
        alt = speed

    elif kp.getKey("s"):
        alt = -speed

    if kp.getKey("d"):
        yaw = aSpeed
        heading += angInterval

    elif kp.getKey("a"): 
        yaw = -aSpeed
        heading -= angInterval

    #if kp.getKey("q"):
        #drone.takeoff()

    if kp.getKey("g"):
        drone.land(); time.sleep(3)

    time.sleep(interval)
    ang += heading
    x += int(trj * math.cos(math.radians(ang)))
    y += int(trj * math.sin(math.radians(ang)))

    return [sides, boards, alt, yaw, x, y]

drone.takeoff()
#This function is responsible for draw the trajetory based on the drone moves
def draw(image, points):
    for point in points:
        cv2.circle(image, (point[0], point[1]), 5, (0, 0, 255), cv2.FILLED)

    cv2.circle(image, points[-1], 8, (0, 255, 0), cv2.FILLED)
    cv2.putText(image, f"({(points[-1][0] - 250)/100}, {(points[-1][1] - 250)/100})m", 
                (points[-1][0] + 10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN, 1,
                (255, 0, 255), 1)

while True:
    values = getInput()      #This vector take the values returned from getInput()
    drone.send_rc_control(values[0], values[1], values[2], values[3])    #Send the respectives values to the drone
    
    image = numpy.zeros((500, 500, 3), numpy.uint8)      #Formation of a matrix in a 1x1 screen
    points.append((values[4], values[5]))                #This vector receives the values of x and y and append
    draw(image, points)                                  #Passing the matrix and the points to be drawn on it

    cv2.imshow("Testing", image)                         #Showing the image on screen
    cv2.waitKey(1)                                       #Delay responsible for avoiding image conflicts