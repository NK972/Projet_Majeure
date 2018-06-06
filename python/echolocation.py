#!/usr/bin/env python
# -*- coding: utf-8 -*-

import qi
import time
#import numpy as np


#qicli call  ALAutonomousLife.setAutonomousAbilityEnabled "All" 0
robot_ip = "134.214.50.49"

def main():
    """
    I should put some doc here
    """
    robot_session = qi.Session()
    robot_session.connect(robot_ip)

    tts = robot_session.service("ALTextToSpeech")
    tts.say("Plop")
    
    motion_service = robot_session.service("ALMotion")
    tracker_service = robot_session.service("ALTracker")

    # First, wake up.
    motion_service.wakeUp()

    # Add target to track.
    targetName = "Sound"
    [distance, confidence] = [0.6, 0.5]
    tracker_service.registerTarget(targetName, [distance, confidence])

    # Then, start tracker.
    tracker_service.track(targetName)

    print "ALTracker successfully started, now show your face to robot!"
    print "Use Ctrl+c to stop this script."

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user"
        print "Stopping..."

    # Stop tracker.
    tracker_service.stopTracker()
    tracker_service.unregisterAllTargets()
    
    #motion_service.rest()

    print "ALTracker stopped."
    
#    audioproxy = robot_session.service("ALAudioDevice")
#    audioproxy.enableEnergyComputation()
    
#    motionproxy = robot_session.service("ALMotion")    
#    motionproxy.setAngles("HeadYaw",0,0.2)
    

#    y_axis = 0
#    x_axis = 0

#    loudest_quadrant = 0
#    #loudest_quadrant_index = 0
#    front_list = []
#    left_list = []
#    rear_list = []
#    right_list = []    


    time.sleep(2)

#    while(1):
#        time.sleep(1)
#        for i in range(10):
#    
#        
#        # Devision by 32768 to normalize the value
#            front = audioproxy.getFrontMicEnergy()/32768.0
#            left = audioproxy.getLeftMicEnergy()/32768.0
#            rear = audioproxy.getRearMicEnergy()/32768.0
#            right = audioproxy.getRightMicEnergy()/32768.0
            
            
    #    if front > loudest_quadrant:
    #        loudest_quadrant_index = i
    #        loudest_quadrant = front
    #    if left > loudest_quadrant:
    #        loudest_quadrant_index = i
    #        loudest_quadrant = left
    #    if rear > loudest_quadrant:
    #        loudest_quadrant_index = i
    #        loudest_quadrant = right
    #    if right > loudest_quadrant:
    #        loudest_quadrant_index = i
    #        loudest_quadrant = rear
    #
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
    #    print "Mics Values :"    
    #    print front
    #    print left
    #    print rear
    #    print right
#            y_axis += front-rear
#            x_axis += right-left
#        y_axis = y_axis/10
#        x_axis = x_axis/10
#        
#       
#        print "Distance : "
#        print(y_axis)
#        print(x_axis)
#        if y_axis > 0 and x_axis > 0:
#            angle = (np.pi/2) - np.arctan(y_axis/x_axis)
#        elif y_axis > 0 and x_axis < 0:
#            angle = -((np.pi/2) + np.arctan(x_axis/y_axis))
#        elif y_axis < 0 and x_axis < 0:
#            angle = -((np.pi/2) + np.arctan(y_axis/x_axis))
#        elif y_axis < 0 and x_axis > 0:
#            angle = (np.pi/2) + np.arctan(y_axis/x_axis)
#        else:
#            angle = 0
        #if False:
#        angle = np.arctan(y_axis/x_axis)
        #angle = np.rad2deg(angle)
        #angle = int(angle)
        #head = Device/SubDeviceList/HeadYaw/Position/Sensor/Value 
        #currentAngle = motionproxy.getAngles("HeadYaw", True)[0]
        #print currentAngle
#        angle = float(angle)    
#        print "Angle :"
#        print angle
#    
#        motionproxy.setAngles("HeadYaw",angle,0.2)

if __name__ == "__main__":
    main()
