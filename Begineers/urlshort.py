import pyshorteners

url = input ( " Enter your url ")

short = pyshorteners.Shortener().tinyurl.short(url)

print(short)