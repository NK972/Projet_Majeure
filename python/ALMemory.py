#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: A Simple class to get & read FaceDetected Events"""

import qi
import sys
import argparse


class myModule(ALModule):
    """
    A simple class to react to face detection events.
    """
    def pythondatachanged(self,strVarName, value):
        """callback when data change"""
        print "datachanged", strVarName, " ", value, " ", strMessage
        

def main(session):
    """
    Initialisation of qi framework and event detection.
    """

    
    
    ALMemory = session.service("ALMemory")
    
    ALMemory.subscribeToEvent("My event","pythonModule", "data")
    
    try:
        #Appuyer sur entrer pour mettre fin au service
        raw_input("\nSpeak to the robot using rules from the just loaded .top file. Press Enter when finished:")
    finally:
        print("\nFin du service ALTabletService") 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="134.214.50.49",
                        help="Robot IP address. On robot or Local Naoqi: use ''.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://{}:{}".format(args.ip))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    pyhtonModule = myModule("pyhtonModule")
    main(session)
    
    