import RPi.GPIO as GPIO
from time import sleep
from utils import _map


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Motor():
    def __init__(self, EnaA, In1A, In2A, EnaB, In1B, In2B):
        # Right motor
        self.EnaA = EnaA
        self.In1A = In1A
        self.In2A = In2A
        # Left motor
        self.EnaB = EnaB
        self.In1B = In1B
        self.In2B = In2B

        # Right motor
        GPIO.setup(self.EnaA, GPIO.OUT)
        GPIO.setup(self.In1A, GPIO.OUT)
        GPIO.setup(self.In2A, GPIO.OUT)
        # Left motor
        GPIO.setup(self.EnaB, GPIO.OUT)
        GPIO.setup(self.In1B, GPIO.OUT)
        GPIO.setup(self.In2B, GPIO.OUT)

        # Right motor
        self.pwmA = GPIO.PWM(self.EnaA, 100);
        self.pwmA.start(0);
        # Left motor
        self.pwmB = GPIO.PWM(self.EnaB, 100);
        self.pwmB.start(0);
    
    def move(self, speed, turn=0, t=0):
        # Normalization takes outputs values between 0 and 1 or -1 and 1
        # User is asked a speed value between 0 and 1
        speed = speed * 100
        #turn = turn * 100

        turn = _map(turn, -1, 1, -speed, speed)

        print(f"speed = {speed}")
        print(f"turn = {turn}")

        # -80 <= turn <= 80
        # Positive value: turn right
        # Negative value: turn left

        rightSpeed = speed
        leftSpeed = speed

        if turn > 0:
            rightSpeed = speed - turn
        elif turn < 0:
            leftSpeed = speed + turn

        # The sum culd be any number between -200 and 200
        # Above 100 and under -100 cases are forced to e in the range
        if leftSpeed > 100: leftSpeed = 100
        elif leftSpeed < -100: leftSpeed = -100

        if rightSpeed > 100: rightSpeed = 100
        elif rightSpeed < -100: rightSpeed = -100

        # abs() gives the module of the value because pwm can't be negative
        # Right motor
        print(f"rightSpeed = {abs(rightSpeed)}")
        self.pwmA.ChangeDutyCycle(abs(rightSpeed));
        self.rightSpeed = rightSpeed
        if rightSpeed > 10:
            GPIO.output(self.In1A, GPIO.LOW)
            GPIO.output(self.In2A, GPIO.HIGH)
        else:
            GPIO.output(self.In1A, GPIO.LOW)
            GPIO.output(self.In2A, GPIO.LOW)

        # Left motor
        print(f"leftSpeed = {abs(leftSpeed)}")
        self.pwmB.ChangeDutyCycle(abs(leftSpeed));
        self.leftSpeed = leftSpeed
        if leftSpeed > 10:
            GPIO.output(self.In1B, GPIO.HIGH)
            GPIO.output(self.In2B, GPIO.LOW)
        else:
            GPIO.output(self.In1B, GPIO.LOW)
            GPIO.output(self.In2B, GPIO.LOW)

        sleep(t)

    def stop(self, t=0):
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)

        sleep(t)

    def debug(self):
        print(f"rightSpeed = {abs(self.rightSpeed)}")
        print(f"leftSpeed = {abs(self.leftSpeed)}")







#######################################

def main():
    # Right motor forward
    motor1.move(.15, .4, 2)
    motor1.stop(2)
    

if __name__ == '__main__':
    motor1 = Motor(25, 24, 23, 27, 9, 22)

    main()