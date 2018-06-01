#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

""" utiliser la tablette """

import qi
import argparse
import sys

def main(session):

    # Se connecte à ALTabletService
    ALTabletService = session.service("ALTabletService")
    # commence une nouvelle application sur la tablette
    ALTabletService.loadApplication("../html/index.html")
    try:
        #Appuyer sur entrer pour mettre fin au service
        raw_input("\nSpeak to the robot using rules from the just loaded .top file. Press Enter when finished:")
    finally:
        print("\nFin du service ALTabletService") 


if __name__ == "__main__":
    """
    Le texte type pour se connecter au Pepper est le suivant:
        
        python aldialog_example_load_file.py --ip $YOUR_ROBOTS_IP_ADDRESS
        
        Pepper1 : ip = 134.214.50.49
        
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot's IP address. If on a robot or a local Naoqi - use '127.0.0.1' (this is the default value).")
    parser.add_argument("--port", type=int, default=9559,
                        help="port number, the default value is OK in most cases")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://{}:{}".format(args.ip))
    except RuntimeError:
        print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
               " Run with -h option for help.\n".format(args.ip))
        sys.exit(1)
    main(session)