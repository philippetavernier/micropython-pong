from machine import Pin,SPI
import sh1106
import time



#on laisse un peu de temps au chargement des librairies
time.sleep(1.5)


spi = SPI(1, baudrate=100000)  #1000000
#spi = SPI(1, baudrate=9600)  #1000000
display = sh1106.SH1106_SPI(128, 128, spi, Pin(9), None, Pin(8))
display.poweron()
display.sleep(False)

WIDTH = 128
HEIGHT = 128
# start with the ball in the center
ball_x = int(WIDTH / 2)
ball_y = int(HEIGHT / 2)
BALL_SIZE = 3 # 2X2 pixels
# set the initial directinon to down to the right
ball_x_dir = 10
ball_y_dir = 1


def draw_ball():
    display.fill_rect(ball_x, ball_y, BALL_SIZE, BALL_SIZE, 1)
    display.text(str(ball_y_dir),5,10,1)
    
'''def update_ball_position():
    ball_x = ball_x + ball_x_dir
    ball_y = ball_y + ball_y_dir
    # update the ball direction if we are at the top or bottom edge
    if ball_y < 3:
        ball_y_dir = 1

    if ball_y > HEIGHT - 3:
        ball_y_dir = -1

    if ball_x < 3:
        ball_x_dir = 1

    if ball_x > WIDTH - 3:
        ball_x_dir = -1
'''

try:

    i=0
    display.fill(0)
    #display.text('Hello',5,10,1)
    while(True):
        #update ball position with the current directions
        #update_ball_position()
        ball_x = ball_x + ball_x_dir
        ball_y = ball_y + ball_y_dir
        # update the ball direction if we are at the top or bottom edge
        if ball_y < 3:
            ball_y_dir = 1
            
        if ball_y > HEIGHT - 3:
            ball_y_dir = -1

        if ball_x < 3:
            ball_x_dir = 1

        if ball_x > WIDTH - 3:
            ball_x_dir = -1
        

        display.fill(0)
        display.line(0,0,i,i,1)
        draw_ball()
        i=i+1
        if(i>128):
            i=0
        str_i=str(i)
        #display.text(str_i,5,10,1)
#         time.sleep(1)
        #time.sleep(0.001)
        #display.text(str(ball_x),5,10,1)
        display.show()
    #display.text('World',5,50,1)
    #display.pixel(20,40,1)

    


except KeyboardInterrupt:
    display.poweroff()  
