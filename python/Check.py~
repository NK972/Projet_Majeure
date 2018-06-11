#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Using ALDialog Methods"""

import qi

import time

robot_ip = "134.214.50.49"

def cheikh_action():
    """
    This example uses ALDialog methods.
    It's a short dialog session with one topic.
    """
    session = qi.Session()
    session.connect(robot_ip)
    #Using ALServices
    tts = session.service("ALTextToSpeech")
    motion_service = session.service("ALMotion")
    life_service = session.service("ALAutonomousLife")
    
    #First deactivate life
    life_service.setAutonomousAbilityEnabled("All",0)
    
    #Check if the programm on the robot is running
    tts.say("Pépére Go")
    
    # Then, wake up.
    motion_service.wakeUp()


    
    print "This is a Pepper check, press Ctrl+c to stop the programm"    
    motion_service.setAngles("LShoulderPitch",-0.349066,0.2)
    motion_service.setAngles("LElbowYaw",0,0.2)
    motion_service.setAngles("LWristYaw",0,0.2)
    motion_service.setAngles("LShoulderRoll",0.174533,0.2)
    motion_service.setAngles("LElbowRoll",-0.174533,0.2)
    motion_service.closeHand("LHand")

    tts.say("Boume!")
    
    motion_service.openHand("LHand")
    motion_service.setAngles("LShoulderRoll",0.226893,0.2)
    motion_service.setAngles("LShoulderPitch",1.0472,0.2)
    motion_service.setAngles("LElbowRoll",-1.18682,0.2) 
    motion_service.setAngles("LElbowYaw",-1.57,0.2)
    motion_service.setAngles("LWristYaw",0.02,0.2)

    time.sleep(1)
    
    motion_service.setAngles("LShoulderPitch",1.76278,0.2)
    motion_service.setAngles("LShoulderRoll",0.1,0.2)
    motion_service.setAngles("LElbowRoll",-0.1,0.2) 
    motion_service.setAngles("LElbowYaw",-1.366593,0.2)
    motion_service.setAngles("LWristYaw",0.04,0.2)
    
    try:
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print
        print "Interrupted by user"
        print "Stopping..."

    #motion_service.rest()

if __name__ == "__main__":
    cheikh_action()
