from djitellopy import tello    #Library for interaction with Tello
from time import sleep          #Library for manipulation of events based in time

drone = tello.Tello()           #Instance of Tello
drone.connect()                 #Stablish connection with the Tello

print("The drone battery level is: ")
print(drone.get_battery())      #Get the drone battery level