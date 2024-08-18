from djitellopy import tello     #Library for interaction with Tello
import cv2                       #Library for capture show on the computer
import numpy                     #Library for matrix operations in Python
import time                      #Library for manipulation of events based in time

drone = tello.Tello()          #Instance of Tello
drone.connect()                #Stablish connection with the Tello

print("The drone battery level is: ")
print(drone.get_battery())     #Get the drone battery level

drone.streamon()               #Gives the frames of the camera to be processed
drone.takeoff()

drone.send_rc_control(0, 0, 25, 0)      #Raising the drone to an average human tall, facilitating face detection
time.sleep(2.2)

proximityRange = [6200, 6800]
pid = [0.4, 0.4, 0]
w, h = 360, 240
pError = 0

#This function is responsible for set the resources of face detecting and perform it on the code
def findFace(image):
    faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imageGray, 1.2, 8)

    faceList = []
    faceArea = []

    for(x, y, w, h) in faces:

        cX = x + w//2      #Calculation of the X-Axis Center
        cY = y + h//2      #Calculation of the Y-Axis Center
        area = w * h       #Calculation of the area

        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)  #Formation of an rectangle in shape of the face detected

        cv2.circle(image, (cX, cY), 5, (0, 255, 0), cv2.FILLED)   #Circle that is positioned on the center of the frame
        faceList.append([cX, cY])
        faceArea.append(area)

    if len(faceList) != 0:
        i = faceList.index(max(faceList))
        return (image, [faceList[i], faceArea[i]])
    else:
        return image, [[0, 0], 0]

#This function is responsible for calculate and obey the restriction of the drone proximity
def shadowing(info, w, pid, pError):
    area = info[1]
    x, y = info[0]
    boards = 0

    error = x - w//2
    speed = (pid[0] * error * pid[1] * (error-pError))
    speed = int(numpy.clip(speed, -100, 100))
    
    if area > proximityRange[0] and area < proximityRange[1]:
        boards = 0
    elif area < proximityRange[0] and area != 0:
        boards = 20
    elif area > proximityRange[1]:
        boards = -20

    print(error, boards)

    if x == 0:
        speed = 0
        error = 0

    drone.send_rc_control(0, boards, 0, speed)
    return error

#capture = cv2.VideoCapture(0)    #This line of code was use to test the software with webcam

while True:
    #_, image = capture.read()    #This line of code was use to test the software with webcam

    image = drone.get_frame_read().frame      #In the infinity loop it keep getting the frame
    image = cv2.resize(image, (w, h))
    image, info = findFace(image)

    pError = shadowing(info, w, pid, pError)

    print("Center: ", info[0], "Area: ", info[1])
    cv2.imshow("Output", image)    #Showing the image on screen

    #Making possible the drone has a land command
    if cv2.waitKey(1) & 0xFF == ord('q'):
        drone.land()
        break