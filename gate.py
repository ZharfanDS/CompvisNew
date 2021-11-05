

from pyfirmata import Arduino, util

import time

def rotate(i,j,k):
    for l in range(i,j,k):
        servo_angle=l
        servo.write(servo_angle)
        
        time.sleep(0.05)
board =Arduino('COM6')

it=util.Iterator(board)
it.start()
servo=board.get_pin('d:9:s')

while True:
    x=int(input("masukkan gambar :"))
    if(x==1):
        rotate(0,90,1)
        time.sleep(5)
        rotate(91,0,-1)

