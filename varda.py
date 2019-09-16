import time
from adafruit_crickit import crickit

def motor_wait():
    #this function moves the servo to original angle, 0
    #and increments its position by two 90 degree steps
    #before rotating back to 0 degrees. Courtesy Adam Hutz!
    #crickit.servo_1.angle sets the angle of your stepper motor
    #time.sleep() asks the processor to wait before executing
       
    print("Moving servo #1: motor_wait()") 
    crickit.servo_1.angle = 0      # right
    time.sleep(1)
    crickit.servo_1.angle = 90     # middle
    time.sleep(1)
    crickit.servo_1.angle = 180    # left
    time.sleep(1)
    crickit.servo_1.angle = 90     # middle
    time.sleep(1)
    crickit.servo_1.angle = 0      # right



def cap_hold():
    print("while holding the sensor, do curious until furious!")#let's get started!
    crickit.servo_1.angle = 0 #initializing our servo at 0
    time.sleep(2) #sleeping for a few seconds after initializing
    
    anger_count = 0 #keep track of how many curious gestures we've exhibited
    while True: #meaning "keep doing everything indented below forever"
        while crickit.touch_1.value: #while capacitive touch sensor is being engaged:
            if crickit.servo_1.angle < 90: #if the servo's angle is less than 30
                for p in range (0, 99, 9): #counting by 4s from 0 to 40 ("p" is arbitrary)
                    crickit.servo_1.angle = p #make the servo's angle equal to the # "p"
                    time.sleep(.5) #sleep a very short time, then repeat this loop until we hit 40
                    anger_count += 1 #keep track of our anger level by adding +1 to "anger_count"

                if anger_count >= 8: #if the anger_count counter gets too big...
                    while crickit.touch_1.value: #and as long as we're /still/ pressing the sensor...
                        crickit.servo_1.angle = 180 #get angry and go to 110!
                        time.sleep(.5) #and try to do it in a half second           
        else:
            print("nothing touching") #oops, we let go of the sensor
            anger_count = 0 #servo calms down, and anger level is reduced to zero
            time.sleep(1) #sleep for a beat


def main():
    # runs code by default!   
  
    print("Hello! DET2019 Servo Test: Starting!")  #print something nice!
    crickit.servo_1.angle = 0                      #set motor to angle '0'
#    motor_wait()
#    motor_conditional()
#    motor_while()
#    motor_for()
    cap_hold()


# the below 'if' statement helps python distinguish the main function.
if __name__ == '__main__':
    main()
