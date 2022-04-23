#!/usr/bin/env python3

import RPi.GPIO as GPIO
import keyboard

#pin assignment with motor driver
movement_forward = 13
movement_backward = 6
steering_right = 19
steering_left = 26

#keyboard button assignment
up = "up"
down = "down"
left = "left"
right = "right"
p_quit = "q"

#initial keypress will be false
keypress = False

#GPIO as output
GPIO.setmode(GPIO.BCM)
GPIO.setup(movement_forward,GPIO.OUT)
GPIO.setup(movement_backward,GPIO.OUT)
GPIO.setup(steering_right,GPIO.OUT)
GPIO.setup(steering_left,GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys


try:
        while True:

            if keyboard.is_pressed(up) and not keypress:
                print("forward")
                GPIO.output(movement_forward,True)
                GPIO.output(movement_backward,False)
                keypress = True
                
            elif keyboard.is_pressed(down) and not keypress:
                print("backward")
                GPIO.output(movement_forward,False)
                GPIO.output(movement_backward,True)
                keypress = True
                
            elif keyboard.is_pressed(right) and not keypress:
                print("right")
                GPIO.output(steering_right,True)
                GPIO.output(steering_left,False)
                keypress = True
                
            elif keyboard.is_pressed(left) and not keypress:
                print("left")
                GPIO.output(steering_right,False)
                GPIO.output(steering_left,True)
                keypress = True
                
            if keypress and not (keyboard.is_pressed(up) or keyboard.is_pressed(down) or  keyboard.is_pressed(left) or  keyboard.is_pressed(right)):
                print("stop")
                GPIO.output(steering_right,False)
                GPIO.output(steering_left,False)
                GPIO.output(movement_forward,False)
                GPIO.output(movement_backward,False)
                keypress = False
            
            if keyboard.is_pressed(p_quit):
                print("program Exit")
                GPIO.output(steering_right,False)
                GPIO.output(steering_left,False)
                GPIO.output(movement_forward,False)
                GPIO.output(movement_backward,False)
                break

            
finally:
    GPIO.cleanup()
