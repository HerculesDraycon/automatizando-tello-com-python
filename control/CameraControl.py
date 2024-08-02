from djitellopy import tello    #Library for interaction with Tello
import cv2

drone = tello.Tello()           #Instance of Tello
drone.connect()                 #Stablish connection with the Tello

drone.streamon()               #Gives the frames of the camera to be processed

while True:
    image = drone.get_frame_read().frame      #In the infinity loop it keep getting the frame
    image = cv2.resize(image, (360, 240))     #Use cv2 to resize the frame in the picture
    cv2.imshow("Captura", image)              #Show the frames flowing in the screen
    cv2.waitKey(1)                            #Necessary delay for the frame show