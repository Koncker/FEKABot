import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Central Flame Sensor
flameCenter = 38
GPIO.setup(flameCenter, GPIO.IN)

#Left Flame Sensor
flameLeft = 37
GPIO.setup(flameLeft, GPIO.IN)

#Right Flame Sensor
flameRight = 40
GPIO.setup(flameRight, GPIO.IN)

#Water Pump
pSwitch = 8
GPIO.setup(pSwitch, GPIO.OUT)

#UltraSound Sensor Left
TRIG1 = 29
ECHO1 = 31

GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)


#UltraSound Sensor Right
TRIG3 = 33
ECHO3 = 35

GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(ECHO3,GPIO.IN)


#Motor Controller
motor1F = 11
motor1B = 7
motor1E = 22

motor2F = 16
motor2B = 13
motor2E = 15

GPIO.setup(motor1F,GPIO.OUT)
GPIO.setup(motor1B,GPIO.OUT)
GPIO.setup(motor1E,GPIO.OUT)
GPIO.setup(motor2F,GPIO.OUT)
GPIO.setup(motor2B,GPIO.OUT)
GPIO.setup(motor2E,GPIO.OUT)

pwm1=GPIO.PWM(22,100)
pwm1.start(100)

pwm2=GPIO.PWM(15,100)
pwm2.start(100)

# Function to move forward
def forward(L,R):
    pwm1.ChangeDutyCycle(L)
    pwm2.ChangeDutyCycle(R)
    GPIO.output(motor1F,GPIO.HIGH)
    GPIO.output(motor1B,GPIO.LOW)
    GPIO.output(motor1E,GPIO.HIGH)
    GPIO.output(motor2F,GPIO.HIGH)
    GPIO.output(motor2B,GPIO.LOW)
    GPIO.output(motor2E,GPIO.HIGH)

# Function to move backward
def backward(L,R):
    pwm1.ChangeDutyCycle(L)
    pwm2.ChangeDutyCycle(R)
    GPIO.output(motor1F,GPIO.LOW)
    GPIO.output(motor1B,GPIO.HIGH)
    GPIO.output(motor1E,GPIO.HIGH)
    GPIO.output(motor2F,GPIO.LOW)
    GPIO.output(motor2B,GPIO.HIGH)
    GPIO.output(motor2E,GPIO.HIGH)

# Function to move right
def right(L,R):
    pwm1.ChangeDutyCycle(L)
    pwm2.ChangeDutyCycle(R)
    GPIO.output(motor1F,GPIO.HIGH)
    GPIO.output(motor1B,GPIO.LOW)
    GPIO.output(motor1E,GPIO.HIGH)
    GPIO.output(motor2F,GPIO.LOW)
    GPIO.output(motor2B,GPIO.HIGH)
    GPIO.output(motor2E,GPIO.HIGH)

# Function to move right while moving forward
def forwRight(L,R):
    pwm1.ChangeDutyCycle(L)
    pwm2.ChangeDutyCycle(R)
    GPIO.output(motor1F,GPIO.HIGH)
    GPIO.output(motor1B,GPIO.LOW)
    GPIO.output(motor1E,GPIO.HIGH)
    GPIO.output(motor2F,GPIO.HIGH)
    GPIO.output(motor2B,GPIO.LOW)
    GPIO.output(motor2E,GPIO.HIGH)

# Function to move right while moving backward
def backRight():
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(50)
    GPIO.output(motor1F,GPIO.LOW)
    GPIO.output(motor1B,GPIO.HIGH)
    GPIO.output(motor1E,GPIO.HIGH)
    GPIO.output(motor2F,GPIO.LOW)
    GPIO.output(motor2B,GPIO.HIGH)
    GPIO.output(motor2E,GPIO.HIGH)

# Function to move left
def left(L,R):
    pwm1.ChangeDutyCycle(L)
    pwm2.ChangeDutyCycle(R)
    GPIO.output(motor1F,GPIO.LOW)
    GPIO.output(motor1B,GPIO.HIGH)
    GPIO.output(motor1E,GPIO.HIGH)
    GPIO.output(motor2F,GPIO.HIGH)
    GPIO.output(motor2B,GPIO.LOW)
    GPIO.output(motor2E,GPIO.HIGH)

# Function to move left while moving forward
def forwLeft(L,R):
    pwm1.ChangeDutyCycle(L)
    pwm2.ChangeDutyCycle(R)
    GPIO.output(motor1F,GPIO.HIGH)
    GPIO.output(motor1B,GPIO.LOW)
    GPIO.output(motor1E,GPIO.HIGH)
    GPIO.output(motor2F,GPIO.HIGH)
    GPIO.output(motor2B,GPIO.LOW)
    GPIO.output(motor2E,GPIO.HIGH)

# Function to move left while moving backward
def backLeft():
    pwm1.ChangeDutyCycle(40)
    pwm2.ChangeDutyCycle(100)
    GPIO.output(motor1F,GPIO.LOW)
    GPIO.output(motor1B,GPIO.HIGH)
    GPIO.output(motor1E,GPIO.HIGH)
    GPIO.output(motor2F,GPIO.LOW)
    GPIO.output(motor2B,GPIO.HIGH)
    GPIO.output(motor2E,GPIO.HIGH)

# Function to stop the motor
def stop():
    GPIO.output(motor1F,GPIO.LOW)
    GPIO.output(motor1B,GPIO.LOW)
    GPIO.output(motor1E,GPIO.LOW)
    GPIO.output(motor2F,GPIO.LOW)
    GPIO.output(motor2B,GPIO.LOW)
    GPIO.output(motor2E,GPIO.LOW)


def ultraSoundLeft():
    sig_time = 0                # signal time, default = 0
    start = time.time()         # receives the start time of the signal sent by the ultrasound
    end = time.time()           # receives the end time when the signal is received by the ultrasound
    
    GPIO.output(TRIG1, True)    # send a signal through the trigger output
    time.sleep(0.00001)         # Time to wait before stopping the output, default = 0.00001 
    GPIO.output(TRIG1, False)   # stop sending a signal through the trigger output

    while GPIO.input(ECHO1) == False:
        start = time.time()     # save a value to the start time when the signal of the echo is not received

    while GPIO.input(ECHO1) == True:
        end = time.time()       # save a value to the end time when the signal of the echo is received

    sig_time = end-start        # time the signal took to go and return

    #CM:
    distanceLeft = sig_time / 0.000058      # calculates the distance that the sound travelled in cm, V = dDistance / dTime

    #print('Left Distance: {} centimeters'.format(distanceLeft))
    return distanceLeft



'''def ultraSoundCenter():
    sig_time = 0
    start = time.time()
    end = time.time()
    
    GPIO.output(TRIG2, True)
    time.sleep(0.00001)
    GPIO.output(TRIG2, False)

    while GPIO.input(ECHO2) == False:
        start = time.time()

    while GPIO.input(ECHO2) == True:
        end = time.time()

    sig_time = end-start

    #CM:
    distanceCenter = sig_time / 0.000058

#    print('Center Distance: {} centimeters'.format(distanceCenter))
    return distanceCenter'''

def ultraSoundRight():
    sig_time = 0
    start = time.time()
    end = time.time()
    
    GPIO.output(TRIG3, True)
    time.sleep(0.00001)
    GPIO.output(TRIG3, False)

    while GPIO.input(ECHO3) == False:
        start = time.time()

    while GPIO.input(ECHO3) == True:
        end = time.time()

    sig_time = end-start

    #CM:
    distanceRight = sig_time / 0.000058

    #print('Right Distance: {} centimeters'.format(distanceRight))
    return distanceRight

def flameCenter():
    return GPIO.input(38)

def flameLeft():
    return GPIO.input(37)

def flameRight():
    return GPIO.input(40)

def waterPump():
    GPIO.output(pSwitch, True)
    time.sleep(1)                   # Sprays the waterPump for time, default = 1 second
    GPIO.output(pSwitch, False)



#We will call this method when the program quits to reset the pwm and cleanup the GPIO so the robot does not immediately resume the last run
def resetBot(): 
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()      # Resets the value of all GPIO pins to 0.
