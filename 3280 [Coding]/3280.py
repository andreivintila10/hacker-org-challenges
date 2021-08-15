import sys

with open('frequencies.txt','r') as f:
  for line in f:
  	if len(line) == 10:
  	  sys.stdout.write(line)