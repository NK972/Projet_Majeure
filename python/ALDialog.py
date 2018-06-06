# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 16:35:20 2018

@author: nicolas.castry
"""

import qi
import argparse
import sys

def RobotDit(session,string): 
    tts = session.service("ALTextToSpeech")
    tts.say(string)

