import cv2                       #Library for capture show on the computer
import KeyboardModule as kp      #Importing the keyboard module
from djitellopy import tello     #Library for interaction with Tello
from time import sleep           #Library for manipulation of events based in time

kp.init()    #Initialize the keyboard module to be able to detect keys being pressed

drone = tello.Tello()          #Instance of Tello
drone.connect()                #Stablish connection with the Tello

print("The drone battery level is: ")
print(drone.get_battery())     #Get the drone battery level

drone.streamon()               #Gives the frames of the camera to be processed

#This method gets the keyboard input and then pass the respective parameter to be returned
def getInput():
    sides, boards, alt, yaw = 0, 0, 0, 0    #This variables set initial parameters for the four ways of movimentation
    speed = 50      #Standard value settled to move the drone

    if kp.getKey("RIGHT"): sides = speed
    elif kp.getKey("LEFT"): sides = -speed

    if kp.getKey("UP"): boards = speed
    elif kp.getKey("DOWN"): boards = -speed

    if kp.getKey("w"): alt = speed
    elif kp.getKey("s"): alt = -speed

    if kp.getKey("d"): yaw = speed
    elif kp.getKey("a"): yaw = -speed

    if kp.getKey("g"): drone.land()

    return [sides, boards, alt, yaw]

drone.takeoff()   #Provisonal command to make the drone takeoff

while True:
    values = getInput()    #This vector take the values returned from getInput()
    drone.send_rc_control(values[0], values[1], values[2], values[3])   #Send the respectives values to the drone

    image = drone.get_frame_read().frame      #In the infinity loop it keep getting the frame
    image = cv2.resize(image, (360, 240))     #Use cv2 to resize the frame in the picture
    cv2.imshow("Captura", image)              #Show the frames flowing in the screen
    cv2.waitKey(1)                            #Necessary delay for the frame show
