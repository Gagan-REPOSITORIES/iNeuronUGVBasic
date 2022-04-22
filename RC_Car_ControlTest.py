#!/usr/bin/env python3

import curses
import RPi.GPIO as GPIO
import time

movement_forward = 6
movement_backward = 13
steering_right = 19
steering_left = 26


GPIO.setmode(GPIO.BCM)
GPIO.setup(movement_forward,GPIO.OUT)
GPIO.setup(movement_backward,GPIO.OUT)
GPIO.setup(steering_right,GPIO.OUT)
GPIO.setup(steering_left,GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                GPIO.output(movement_forward,True)
                GPIO.output(movement_backward,False)
                
            elif char == curses.KEY_DOWN:
                GPIO.output(movement_forward,False)
                GPIO.output(movement_backward,True)
                
            elif char == curses.KEY_RIGHT:
                GPIO.output(steering_right,True)
                GPIO.output(steering_left,False)
                #GPIO.output(movement_forward,True)
                #GPIO.output(movement_backward,False)
                
            elif char == curses.KEY_LEFT:
                GPIO.output(steering_right,False)
                GPIO.output(steering_left,True)
                #GPIO.output(movement_forward,True)
                #GPIO.output(movement_backward,False)
                
            elif char == ord('s'):
                GPIO.output(steering_right,False)
                GPIO.output(steering_left,False)
                GPIO.output(movement_forward,False)
                GPIO.output(movement_backward,False)
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
