#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use getData Method to Use FSR Sensors"""

import qi
import argparse
import sys


class MyModule:
    """
    Wow, there should be some doc here too
    """
    def __init__(self, session):
        """
        """
        print "MyModule init"
        self.session = session
        self.tts = self.session.service("ALTextToSpeech")
        self.memory = self.session.service("ALMemory")

        self.watch_head_subscriber = None
        self.watch_head_id = None


    def __del__(self):
        """
        """
        self.stop_watch_head_touch()


    def say_something(self, something):
        """
        """
        print "MyModule.say_something"
        self.tts.say(something)


    def start_watch_head_touch(self):
        """
        """
        if self.watch_head_subscriber is None:
            self.watch_head_subscriber = self.memory.subscriber("FrontTactilTouched")
            self.watch_head_id = self.watch_head_subscriber.signal.connect(self._watch_head_callback)

    def stop_watch_head_touch(self):
        """
        """
        try:
            if self.watch_head_subscriber is not None:
                self.watch_head_subscriber.signal.disconnect(self.watch_head_id)
        except Exception as e:
            print "Exception in stop_watch_subscriber: %s" % e


    def _watch_head_callback(self, value):
        """
        """
        if value == 1:
            self.say_something("On a touché ma tête")

def main(session):
    """
    This example uses the getData method to use FSR sensors.
    """
    # Get the service ALMemory.

    memory_service = session.service("ALMemory")
    app = qi.Application(url="tcp://134.214.50.49:9559")
    app.start()

    s = app.session
    my_module = MyModule(s)
    s.registerService("MyModule", my_module)

    app.run()

    # Get The Left Foot Force Sensor Values
    """ 
    LFsrFL = memory_service.getData("Device/SubDeviceList/LFoot/FSR/FrontLeft/Sensor/Value")
    LFsrFR = memory_service.getData("Device/SubDeviceList/LFoot/FSR/FrontRight/Sensor/Value")
    LFsrBL = memory_service.getData("Device/SubDeviceList/LFoot/FSR/RearLeft/Sensor/Value")
    LFsrBR = memory_service.getData("Device/SubDeviceList/LFoot/FSR/RearRight/Sensor/Value")

    print( "Left FSR [Kg] : %.2f %.2f %.2f %.2f" %  (LFsrFL, LFsrFR, LFsrBL, LFsrBR) )

    # Get The Right Foot Force Sensor Values
    RFsrFL = memory_service.getData("Device/SubDeviceList/RFoot/FSR/FrontLeft/Sensor/Value")
    RFsrFR = memory_service.getData("Device/SubDeviceList/RFoot/FSR/FrontRight/Sensor/Value")
    RFsrBL = memory_service.getData("Device/SubDeviceList/RFoot/FSR/RearLeft/Sensor/Value")
    RFsrBR = memory_service.getData("Device/SubDeviceList/RFoot/FSR/RearRight/Sensor/Value")

    print( "Right FSR [Kg] : %.2f %.2f %.2f %.2f" %  (RFsrFL, RFsrFR, RFsrBL, RFsrBR) )
    """


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="134.214.50.49",
                        help="Robot IP address. On robot or Local Naoqi: use '134.214.50.49'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
    # Starting the dialog engine - we need to type an arbitrary string as the identifier
    # We subscribe only ONCE, regardless of the number of topics we have activated

    try:
        raw_input("\nSpeak to the robot using rules from the just loaded .top file. Press Enter when finished:")
    finally:
        print("DC")
