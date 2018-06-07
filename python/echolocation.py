#!/usr/bin/env python
# -*- coding: utf-8 -*-

import qi



#qicli call  ALAutonomousLife.setAutonomousAbilityEnabled "All" 0
robot_ip = "134.214.50.49"

def main():
    """
    I should put some doc here
    """
    #New session
    robot_session = qi.Session()
    robot_session.connect(robot_ip)

	#Using ALServices
    tts = robot_session.service("ALTextToSpeech")
    motion_service = robot_session.service("ALMotion")
    tracker_service = robot_session.service("ALTracker")
    life_service = robot_session.service("ALAutonomousLife")
    

    
    #First deactivate life
    life_service.setAutonomousAbilityEnabled("All",0)
    
    #Check if the programm on the robot is running
    tts.say("Dihé")
    
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
    
    
    # Example showing how to set the stiffness to 1.0.
    # Beware, doing this could be dangerous, it is safer to use the
    #   stiffnessInterpolation method which takes a duration parameter.
#    names  = 'Move'
#    # If only one parameter is received, this is applied to all joints
#    stiffnesses  = 1.0
#    motion_service.setStiffnesses(names, stiffnesses)

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
        
#    motionproxy = robot_session.service("ALMotion")    
#    motionproxy.setAngles("HeadYaw",0,0.2)
    
  
if __name__ == "__main__":
    main()
