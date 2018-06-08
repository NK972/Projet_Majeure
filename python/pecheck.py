#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Using ALDialog Methods"""

import qi
import time

robot_ip = "134.214.50.49"

def check(tts,motion_service):

    print "This is a Pepper check"    
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
    motion_service.setAngles("LWristYaw",0.02,0.2)

    time.sleep(1)
    
    motion_service.setAngles("LShoulderPitch",1.57,0.2)
    motion_service.setAngles("LShoulderRoll",0.02,0.2)
    motion_service.setAngles("LElbowRoll",-0.02,0.2) 
    motion_service.setAngles("LElbowYaw",-0.02,0.2)
    motion_service.setAngles("LWristYaw",-1.57,0.2)

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
    tracker_service = session.service("ALTracker")
    life_service = session.service("ALAutonomousLife")

    #First deactivate life
    life_service.setAutonomousAbilityEnabled("All",0)
    
    #Check if the programm on the robot is running
    tts.say("Pepeur Go")
    
    # Then, wake up.
    motion_service.wakeUp()

    # Add target to track.
    targetName = "Sound"
    [distance, confidence] = [0.6, 0.5]
    tracker_service.registerTarget(targetName, [distance, confidence])

    # set mode
    mode = "Move"
    tracker_service.setMode(mode)

    # Then, start tracker.
    tracker_service.track(targetName)   
    
    print "ALTracker successfully started, now show your face to robot!"
    print "Use Ctrl+c to stop this script."

    #Check launching 
    speech=session.service("ALSpeechRecognition")
    speech.setVocabulary(["check" "tchèque" "topla"], 1)
    a=speech.WordRecognized("WordRecognized")
    print a
    if a==1:
        check(tts,motion_service)
        a=0
    
        
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
    



if __name__ == "__main__":
    main()
