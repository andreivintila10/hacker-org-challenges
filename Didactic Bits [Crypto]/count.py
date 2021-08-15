import sys

filename = "message.txt"
count_a = count_b = 0
bit_string = ""

with open(filename) as f:
  while True:
    c = f.read(1)
    if c == 'a':
      count_a += 1
      bit_string += "0"
    elif c == 'b':
      count_b += 1
      bit_string += "1"
    if not c:
      break

    sys.stdout.write(c)

print("\n");
print("Number of a: " + str(count_a))
print("Number of b: " + str(count_b))
print("Bits: " + bit_string)
print("\n");
for index in range(23):
  left = index * 8
  right = left + 8
  byte_int = int(bit_string[left:right], 2)

  byte_char = str(chr(byte_int))
  sys.stdout.write(byte_char)