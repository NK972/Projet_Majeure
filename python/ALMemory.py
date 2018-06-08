#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: A Simple class to get & read FaceDetected Events"""

import qi
import time
import sys
import argparse

from ALDialog import RobotDit
from translate import Translate
from Blagues import recupBlague

session = None
memory = None

def write(string):
    fichier = open("Communication/Communication_entre_python.txt","a+")
    fichier.write(string+"\n")
    fichier.close()
    
def read():
    fichier = open("Communication/Communication_entre_python.txt","r")
    file_line = fichier.readlines();
    for x in file_line:
        print(x)
    fichier.close()
    return file_line[-1]
    
class HumanGreeter(object):
    """
    A simple class to react to face detection events.
    """

    def __init__(self, app):
        """
        Initialisation of qi framework and event detection.
        """
        global memory
        global session
        super(HumanGreeter, self).__init__()
        app.start()
        session = app.session
        # Get the service ALMemory.
        self.memory = session.service("ALMemory")
        # Connect the event callback.
        #
        self.subscriber_acceuil = self.memory.subscriber("accueil")
        self.subscriber_acceuil.signal.connect(self.accueil_event)
        #
        self.subscriber_accueil_0 = self.memory.subscriber("accueil_0")
        self.subscriber_accueil_0.signal.connect(self.accueil_0_event)      
        #
        self.subscriber_presentation_prepa  = self.memory.subscriber("presentation_prepa")
        self.subscriber_presentation_prepa.signal.connect(self.presentation_prepa_event)          
        #
        self.subscriber_choix = self.memory.subscriber("choix")
        self.subscriber_choix.signal.connect(self.choix_event)          
        #
        self.subscriber_Presentation_filiere = self.memory.subscriber("Presentation_filiere")
        self.subscriber_Presentation_filiere.signal.connect(self.Presentation_filiere_event)  
        #
        self.subscriber_Presentation_filiere1 = self.memory.subscriber("Presentation_filiere1")
        self.subscriber_Presentation_filiere1.signal.connect(self.Presentation_filiere1_event)
        #
        self.subscriber_Blague = self.memory.subscriber("Blague")
        self.subscriber_Blague.signal.connect(self.Blague_event)
        #
        self.subscriber_Translate = self.memory.subscriber("translate")
        self.subscriber_Translate.signal.connect(self.Translate_event)

        #
        self.subscriber_Translate_vers_Java = self.memory.subscriber("Translate_vers_Java")
        self.subscriber_Translate_vers_Java.signal.connect(self.Translate_vers_Java_event)
        
        # Get the services ALTextToSpeech and ALFaceDetection.
        self.tts = session.service("ALTextToSpeech")
        self.face_detection = session.service("ALFaceDetection")
        self.face_detection.subscribe("HumanGreeter")
        self.got_face = False

    def accueil_event(self, value):
        print("Event : Accueil_event")
    def accueil_0_event(self, value):
        print("accueil_0_event")
    def presentation_prepa_event(self, value):
        print("presentation_prepa_event")
    def choix_event(self, value):
        print("choix_event")
    def Presentation_filiere_event(self, value):
        print("Presentation_filiere_event")
    def Presentation_filiere1_event(self, value):
        print("Presentation_filiere1_event")
    def Blague_event(self, value):
        print("une demande de blague")
        write("DemandeDeBlague")
        RobotDit(session,recupBlague())
    def Translate_event(self, value):
        val = self.memory.getData("translate")
        print("Evenement : Tranlate ??")
        if(val!="1"):
            print("Evenement : une demande de traduction de "+val)
            t =Translate(val)
            self.memory.raiseEvent("Translate_vers_Java", t )
    def Translate_vers_Java_event(self, value):
        print("Evenement : Envoie de la traduction vers java"+value)    
        print(value)
    def check(self, value):
        


    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print "Starting HumanGreeter"
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print "Interrupted by user, stopping HumanGreeter"
            self.face_detection.unsubscribe("HumanGreeter")
            #stop
            sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="134.214.50.49",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    try:
        # Initialize qi framework.
        connection_url = "tcp://" + args.ip + ":" + str(args.port)
        app = qi.Application(["HumanGreeter", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    human_greeter = HumanGreeter(app)
    human_greeter.run()