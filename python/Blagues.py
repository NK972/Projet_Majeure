# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:13:49 2018

@author: nicolas.castry
"""

def recupBlague():
    import urllib, json
    url = "https://www.chucknorrisfacts.fr/api/get?data=nb:1;tri:alea"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data[0]["fact"]
