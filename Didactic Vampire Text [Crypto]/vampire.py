import sys

with open("text.txt") as f:
	byte = str(f.read(1))
	while byte:
		if byte.isupper():
		  sys.stdout.write(byte)
		byte = str(f.read(1))