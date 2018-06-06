#!/usr/bin/env python
# -*- coding: utf-8 -*-

import qi
#import time
import numpy as np

robot_ip = "134.214.50.49"

def main():
    """
    I should put some doc here
    """
    robot_session = qi.Session()
    robot_session.connect(robot_ip)

    tts = robot_session.service("ALTextToSpeech")
    tts.say("hé?")

    audioproxy = robot_session.service("ALAudioDevice")
    audioproxy.enableEnergyComputation()

#    loudest_quadrant = 0
#    #loudest_quadrant_index = 0
#    front_list = []
#    left_list = []
#    rear_list = []
#    right_list = []
    print("Localizing...")
    #for i in range(20):
    #    time.sleep(0.05)
        # Devision by 32768 to normalize the value
    front = audioproxy.getFrontMicEnergy()#/32768.0
    left = audioproxy.getLeftMicEnergy()#/32768.0
    rear = audioproxy.getRearMicEnergy()#/32768.0
    right = audioproxy.getRightMicEnergy()#/32768.0
# """   
#    if front > loudest_quadrant:
##        loudest_quadrant_index = i
#        loudest_quadrant = front
#    if left > loudest_quadrant:
##        loudest_quadrant_index = i
#        loudest_quadrant = left
#    if rear > loudest_quadrant:
##        loudest_quadrant_index = i
#        loudest_quadrant = right
#    if right > loudest_quadrant:
##        loudest_quadrant_index = i
#        loudest_quadrant = rear
#            """
#    front_list.append(front)
#    left_list.append(left)
#    rear_list.append(rear)
#    right_list.append(right)
#    loudest_front = front_list[loudest_quadrant_index] - np.mean(front_list)
#    loudest_left = left_list[loudest_quadrant_index] - np.mean(left_list)
#    loudest_rear = rear_list[loudest_quadrant_index] - np.mean(rear_list)
#    loudest_right = right_list[loudest_quadrant_index] - np.mean(right_list)
#    y_axis = loudest_front - loudest_rear
#    x_axis = loudest_right - loudest_left    
    print "Mics Values :"    
    print front
    print left
    print rear
    print right
    y_axis = front-rear
    x_axis = right-left
    print "Distance : "
    print(y_axis)
    print(x_axis)
    if y_axis > 0 and x_axis > 0:
        angle = (np.pi/2) - np.arctan(y_axis/x_axis)
    elif y_axis > 0 and x_axis < 0:
        angle = -((np.pi/2) + np.arctan(x_axis/y_axis))
    elif y_axis < 0 and x_axis < 0:
        angle = -((np.pi/2) + np.arctan(y_axis/x_axis))
    elif y_axis < 0 and x_axis > 0:
        angle = (np.pi/2) + np.arctan(y_axis/x_axis)
    else:
        angle = 0
    #if False:
     #   angle = np.rad2deg(angle)


    print "Angle :"
    print angle

    
   
    #tts.say(front)


if __name__ == "__main__":
    main()
