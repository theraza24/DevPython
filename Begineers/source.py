#Write a python program to get the source code of the any website

import urllib.request

print(urllib.request.urlopen("https://www.skatestv.com/").read())
