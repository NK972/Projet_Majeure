
import Algorithmia

import urllib, json
url = "https://www.chucknorrisfacts.fr/api/get?data=nb:1;tri:alea"
response = urllib.urlopen(url)
data = json.loads(response.read())

print data[0]["fact"]
