# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:10:38 2018

@author: thomas.lesbros
"""

from naoqi import ALProxy
import time
check = 0


# create python module
class myModule(ALModule):
  """python class myModule test auto documentation: comment needed to create a new python module"""


  def addEau():
    Liste_Commande = memProxy.getData("Liste_Commande")
    Liste_Commande.append("eau")
    print(Liste_Commande)

  def _pythonPrivateMethod(self, param1, param2, param3):
    global check


broker = ALBroker("pythonBroker","10.0.252.184",9999,"naoverdose.local",9559)


# call method
try:
    
  pythonModule = myModule("pythonModule")
  prox = ALProxy("ALMemory","localhost",9559)
  #prox.insertData("val",1) # forbidden, data is optimized and doesn't manage callback
  prox.subscribeToEvent("eve_commande_eau","pythonModule", "addEau") #  event is case sensitive !

except Exception,e:
  print "error"
  print e
  exit(1)

while (1):
  time.sleep(2)