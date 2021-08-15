with open("fl.txt") as f:
  print(f)
  byte = ord(f.read(1))
  while byte:
    print(str(byte))
    byte = f.read(1)