import urllib.request
from time import sleep
from datetime import datetime


print("Started at: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

try:
	f = open("result3.txt", "w")

	while True:
	  contents = urllib.request.urlopen("http://www.hacker.org/challenge/misc/minuteman.php").read()
	  datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	  f.write(str(datetime_now) + "\n" + str(contents) + "\n\n")
	  sleep(45)

finally:
	f.close()