# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 16:09:51 2018

@author: nicolas.castry
"""

import Algorithmia

def Translate(string):
    input = {
      "action": "translate",
      "text": string
    }
    client = Algorithmia.client('sim61hYbFv8RiXBOE0Vclt62ifF1')
    algo = client.algo('translation/GoogleTranslate/0.1.1')
    print(algo.pipe(input))
    
    
## Test
    
#string="Ich habe kein zeit!"
#string2="Je suis le robot Pepper et je suis gentil"
#Translate(string)
#Translate(string2)



