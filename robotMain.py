# import curses,time, motorController module, os and randint from random
import curses, time
import motorController as motor
from random import randint
import os #This is added to shutdown the Raspberry Pi

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()  
curses.cbreak()
curses.halfdelay(3)
screen.keypad(True)

def callback(flameCenter):
        print ("Flame Detected")

goingForward = False
goingBackward = False
classMode = 0

try:
        while True:
            motor.stop()
            char = screen.getch()

            if char == ord('q'):
                break

            if char == ord('S'): #We shutdown the pi with capital S
                os.system ('sudo shutdown now') #shutdown now

            elif char == curses.KEY_UP:
                goingForward = True
                goingBackward = False
                print("Moving Forward")
                motor.forward(50,50)

            elif char == curses.KEY_DOWN:
                goingForward = False
                goingBackward = True
                print("Moving Backward")
                motor.backward(50,50)

            elif char == curses.KEY_RIGHT and goingForward:
                motor.forwRight(75,50)
                print("Moving Front/Right")

            elif char == curses.KEY_RIGHT and goingBackward:
                motor.backRight(75,50)
                print("Moving Back/Right")

            elif char == curses.KEY_RIGHT:
                motor.right(50,50)
                print("Moving Right")

            elif char == curses.KEY_LEFT and goingForward:
                motor.forwLeft(50,75)
                print("Moving Front/Left")

            elif char == curses.KEY_LEFT and goingBackward:
                motor.backLeft(50,75)
                print("Moving Back/Left")

            elif char == curses.KEY_LEFT:
                motor.left(50,50)
                print("Moving Left")

            elif char == 10:    #Stop motors if Enter is pressed
                goingForward = False
                goingBackward = False
                print("Motor Stopping")
                motor.stop()

            #if char == ord('u'):
            if classMode == 1 or char == ord('u'):
                print("Entering Class Presentation Mode")
                while True:
                        L = 30
                        R = 37
                        motor.forward(L,R)
                        char = screen.getch()
                        if char == ord ('q'):
                                print ("Quitting class navigation")
                                classMode = 0
                                break

                        #elif char == ord('m'):
                        #        motor.forward(L,R)

                        elif motor.flameCenter() == 1:
                                print ("Center Flame doing something")
                                while motor.flameCenter() == 1:
                                        motor.stop()
                        #                motor.waterPump()
                                motor.backward(randint(0,100),randint(0,100))
                                time.sleep(2)
                                motor.forward(L,R)

                        elif motor.flameLeft() == 1:
                                motor.stop()
#                                print("Left flame detected. Stopping motor")
                                if motor.flameCenter() == 0:
#                                        print("flameCenter = 0 Left Detected")
                                        motor.left(30,30)

                        elif motor.flameRight() == 1:
                                motor.stop()
#                                print("Right flame detected. Stopping motor")
                                if motor.flameCenter() == 0:
#                                        print("flameCenter = 0 Right Detected")
                                        motor.right(30,30)

                        elif motor.ultraSoundRight() < 30:
                                while motor.ultraSoundRight() < 30:
                                        goingForward = False
                                        #BraitenBerg Left
                                        distanceL = motor.ultraSoundRight()
                                        BLeft = (1/distanceL) * 200
                                        if (BLeft + L) > 100:
                                                BLeft = 100 - L
                                        #BraitenBerg Right
                                        BRight = (1/distanceL) * 200
                                        if (R - BRight) < 0:
                                                BRight = R
                                        motor.right(L+BLeft,R+BRight)
                                        time.sleep(0.25)
                                
                                motor.forward(L,R)


                        elif motor.ultraSoundLeft() < 20:
                                while motor.ultraSoundLeft() < 20:
                                        goingForward = False
                                        #BraitenBerg Left
                                        distanceR = motor.ultraSoundLeft()
                                        BRight = (1/distanceR) * 200
                                        if (BRight + R) > 100:
                                                BRight = 100 - R
                                        #BraitenBerg Right
                                        BLeft = (1/distanceR) * 200
                                        if (L - BLeft) < 0:
                                                BLeft = L
                                        motor.left(L+BLeft,R+BRight)
                                        time.sleep(0.25)
                                
                                motor.forward(L,R)
          
finally:
    #Close curses properly, turn echo back on. Also reset the bot through motor.
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    motor.resetBot()
