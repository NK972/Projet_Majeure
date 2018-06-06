# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 08:40:45 2018

@author: CASTRY
"""

from translate import Translate 

def main():
    initFichieTxt()
    write("Hello World")
    write("bizar")  
    write("Merdeeeeeeee")
    
    print(read())

def initFichieTxt():
    fichier = open("Communication/Communication_entre_python.txt","w")
    fichier.close()
    
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


if __name__ == "__main__":
   main()