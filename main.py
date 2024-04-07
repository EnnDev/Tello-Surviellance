# Nathaniel Igot
# This is a simple project intended for fun and educational purposes
# This project allows one to control a drone through their keyboard

from djitellopy import tello
import cv2

# This creates a tello object which allows for connection
drone = tello.Tello()
drone.connect()
# This will print out the battery life
print('The battery life is at: '+str(drone.get_battery())+'%')

drone.streamon()

while True:
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (640,360))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # This is needed for color correction
    cv2.imshow("Image",img)
    cv2.waitKey(1)