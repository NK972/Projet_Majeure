#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Using ALDialog Methods"""

import qi

import time

robot_ip = "134.214.50.49"

def main():
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
    motion_service.closeHand("LHand")
    motion_service.setAngles("LShoulderPitch",-0.349066,0.2)
    motion_service.setAngles("LElbowYaw",0,0.2)
    motion_service.setAngles("LWristYaw",0,0.2)
    motion_service.setAngles("LShoulderRoll",0.174533,0.2)
    motion_service.setAngles("LElbowRoll",-0.174533,0.2)
    motion_service.closeHand("LHand")
    
    time.sleep(0.3)
    motion_service.closeHand("LHand")
    tts.say("Boume!")
    
    motion_service.openHand("LHand")
    motion_service.setAngles("LShoulderRoll",0.174533,0.2)
    motion_service.setAngles("LShoulderPitch",1.57,0.2)
    motion_service.setAngles("LElbowRoll",-1.39626,0.2) 
    motion_service.setAngles("LElbowYaw",-1.57,0.2)
    motion_service.setAngles("LWristYaw",0,0.2)

    time.sleep(1)
    
    motion_service.setAngles("LShoulderPitch",1.57,0.2)
    motion_service.setAngles("LShoulderRoll",0,0.2)
    motion_service.setAngles("LElbowRoll",0,0.2) 
    motion_service.setAngles("LElbowYaw",0,0.2)
    motion_service.setAngles("LWristYaw",-1.57,0.2)
    
    try:
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print
        print "Interrupted by user"
        print "Stopping..."

    #motion_service.rest()

if __name__ == "__main__":
    main()
