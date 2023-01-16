from MotorModule2 import Motor
from LineDetectionModule import getLaneCurve
import WebcamModule
import cv2
 

# EnaA, In1A, In2A, EnaB, In1B, In2B
motor = Motor(25, 24, 23, 27, 9, 22)


def main(): 
    img = WebcamModule.getImg()
    curveVal = getLaneCurve(img)
 
    sen = 1  # SENSITIVITY
    #maxVAl= 0.3 # MAX SPEED

    # Normalization
    if curveVal > 1: curveVal = 1
    if curveVal < -1: curveVal = -1
    
    if curveVal > 0:
        #sen = 1.3

        # If curveVal < .05 don't turn
        # Different parameters depending on the motors' syncronization
        if curveVal < 0.1: curveVal = 0
    else:
        if curveVal > -0.1: curveVal = 0

    turn = -curveVal * sen

    # Normalization
    if turn > 1: turn = 1
    if turn < -1: turn = -1

    print(turn)
    motor.move(0.15, turn, 0.05)
    #cv2.waitKey(1)
     
 
if __name__ == '__main__':
    while True:
        main()
