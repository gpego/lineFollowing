# EnA = speed control pin
# In1A, In2A = direction control pins

import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
 
class Motor():
    def __init__(self, EnaA, In1A, In2A):
        self.EnaA = EnaA
        self.In1A = In1A
        self.In2A = In2A
        
        # Decleare pins as output
        GPIO.setup(self.EnaA,GPIO.OUT); GPIO.setup(self.In1A,GPIO.OUT); GPIO.setup(self.In2A,GPIO.OUT)
        
        # PWM pin = speed control pin
        # 2nd argument = frequency
        self.pwmA = GPIO.PWM(self.EnaA, 100);
        self.pwmA.start(0); # Starting speed = 0
        self.mySpeed = 0
 
    def move(self, speed = 0.1, turn = 0, t = 0):
        # turn:
        # Positive value: <-- left turn
        # Negative value: --> right turn
        speed *= 100
        turn *= 70
        leftSpeed = speed - turn
        rightSpeed = speed + turn
 
        if leftSpeed > 00: leftSpeed = 100
        elif leftSpeed <- 100: leftSpeed = -100
        if rightSpeed > 100: rightSpeed = 100
        elif rightSpeed <- 100: rightSpeed = -100

        # 0 <= Duty Cycle <= 100
        # speed = Duty Cycle
        self.pwmA.ChangeDutyCycle(abs(leftSpeed))
        #self.pwmB.ChangeDutyCycle(abs(rightSpeed))

        # Right motor ON (BACKWARD)
        if leftSpeed > 0: GPIO.output(self.In1A,GPIO.HIGH); GPIO.output(self.In2A,GPIO.LOW)
        # Right motor ON (FORWARD)
        else: GPIO.output(self.In1A,GPIO.LOW); GPIO.output(self.In2A,GPIO.HIGH)

        sleep(t)
 
    def stop(self,t = 0):
        self.pwmA.ChangeDutyCycle(0);
        self.mySpeed = 0

        sleep(t)    # Delay in [s]


def main():
    motor.move(0.5, 0 ,2)
    motor.stop(2)
    motor.move(-0.5, 0, 2)
    motor.stop(2)
    motor.move(0, 0.5, 2)
    motor.stop(2)
    motor.move(0, -0.5, 2)
    motor.stop(2)
 
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    #25, 24, 23, 9, 22, 27
    EnaA, In1A, In2A = 25, 24, 23
    EnaB, In1B, In2B = 9, 22, 27
    motor1 = Motor(EnaA, In1A, In2A)
    motor2 = Motor(EnaB, In1B, In2B)
    self = .25

    while True:
        # Right motor BACKWARD
        motor1.move(0)

        # Left motor FORWARD
        motor2.move(0)

